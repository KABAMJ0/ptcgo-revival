# The scripted tutorial funnel — what drives each step

Read out of the shipped client (`pie-src.dll`, 2020 build) with `mddump.py` /
`mdump.py` / `find.py` and the obfuscated string table (see "How this was read").
The scene is `ExtendedTutorial`; the state machine is
`pie.code.pie.gameModules.trainerChallenge.FunnelState`.

## The states, and what moves the client out of each

| state | value | what advances it |
| --- | --- | --- |
| `UNSET` | 0 | client-side on sign-in, from its own NUX account settings |
| `TutorialGame1Intro` | 1 | the scene's intro runs; closing the scene disposes it (`f.E::Dispose` → `NUXManager.AdvanceFunnel`) |
| `TutorialGame1` | 2 | `TutorialPlayGame {index: 0}` — the server starts the match |
| `TutorialGame2Intro` | 3 | as the first intro; the scene reloads status (`subMode "tutorial"`) |
| `TutorialGame2` | 4 | `TutorialPlayGame {index: 1}` |
| `TrainingIntro` | 5 | the scene's own dispose (`AdvanceFunnel`) |
| `Training` | 6 | `AdvanceFunnel` → `triggerOpenBoosterFunnel`, which opens a pack from the collection |
| `OpenBooster` | 7 | `NUXManager.EndOpenPackStep` after the pack-opening flow |
| `OutOfFunnel` | 8 | — |

`NUXManager.ProcessFunnelState` maps each state to a scene or an action, read
from its jump table (`switch (state - 1)`):

| state | `FullScreenScenario` | scene / action |
| --- | --- | --- |
| `TutorialGame1Intro` | 1 | stays where it is |
| `TutorialGame1` | 1 | the manager's configured scene (`ExtendedTutorial`) |
| `TutorialGame2Intro`, `TutorialGame2` | 49 | the same scene |
| `TrainingIntro` | — | `ResumingTrainingMode = 1`, scene `ExtendedTutorial` |
| `Training` | — | `triggerOpenBoosterFunnel()` |
| `OpenBooster` | — | nothing |

`NUXManager.AdvanceFunnel` is the other mover (called from the scene's dispose,
`f.E::Dispose`), and it is what walks a finished player from the second match to
`TrainingIntro` and then to `Training`, where the booster actually opens.

`o.b::updateTutorialMatchStatus` is the only reader of
`HasAvailableTutorialMatches`. Its logic, once the branches are resolved:

```
if (msg.HasAvailableMatches) return;                 // another match follows
if (funnelSetting == Training) return;               // already past the matches
nuXManager.CurrentFunnelState = (funnelSetting == TrainingIntro) ? TrainingIntro
                                                                 : OpenBooster;
funnelSetting.SetValue(CurrentFunnelState);
```

Note what that means for a player standing on the second match (`4`): the flag
sends them straight to `OpenBooster`, and `ProcessFunnelState` does nothing for
`OpenBooster`, so `triggerOpenBoosterFunnel` — the step that opens the pack —
never runs. The `== TrainingIntro ? TrainingIntro : OpenBooster` branch only
behaves well when the player has already advanced to `TrainingIntro`. So the
server does not send it after a win; it answers it only when Play is pressed and
there is no match left, where the alternative is a scene that does nothing.

The funnel value itself lives in the client's account settings
(`SetAccountSettings {settings: {int: int}}`), which this server already stores.

## The messages

| direction | message | payload | meaning |
| --- | --- | --- | --- |
| client → server | `LeagueAndGymModeGetStatus` | `{subMode: "tutorial"}` | the funnel scene wants its state |
| client → server | `LeagueAndGymModeGetRewards` | `{subMode: "tutorial"}` | and its reward schedule |
| client → server | `TutorialPlayGame` | `{index: int}` | Play on match panel `index` (0-based) |
| client → server | `LeagueAndGymModePlayGame` | `{subMode: "tutorial"}` | the *intro's* Play, which carries no index |
| client → server | `TutorialClaimRewards` | `{}` | collect the pending payout |
| server → client | `LeagueAndGymModeStatus` | see `notes/league-dto.md` | opponents + `waitingForRewards` + `losses` |
| server → client | `LeagueAndGymModeRewards` | `totalRewardSchedule` keyed 0..n-1 | one entry per match panel |
| server → client | `HasAvailableTutorialMatches` | `{hasAvailableMatches: bool}` | whether another scripted match follows |

`StartTutorial`, `StartTutorialPostLogin` and `SetTutorialPack` are **not**
client messages: the first is a `MonoBehaviour` method, the second a scene name,
the third a local model setter, and no string literal for any of them exists in
the assembly. Answering them cannot advance anything.

`TutorialDeckUnlock {unlock: ArchetypeID}` exists as a message type but has no
reader in this build (no IL references it, and no TypeSpec mentions it), so
sending it does nothing.

## The deck a tutorial match is played with

`#4315 b::MoveNext` — the shared PvE Play coroutine — builds the match like this:

```
match.trainer = GetAITrainerByName(funnel == TutorialGame1 ? "Ella" : "Zach");
match.deck    = K.U::NuxQuickplayDeck();
if (index >= 0) SendMessage(TutorialPlayGame(index));
else            SendMessage(LeagueAndGymModePlayGame("tutorial"));
```

`K.U::NuxQuickplayDeck` returns the first deck **the player owns** whose first
deck colour is `11`, else a random owned deck, else null. A player who owns no
deck therefore has nothing to field — which is why a fresh account could not
start the tutorial match. The server fielding side matches this by using the
player's first complete deck and granting a starter deck from the catalogue when
they own none.

## How the rewards are read

`LeagueAndGymModeStatus` is parsed by `#4322 F::MoveNext`, which sets
`PvEOpponentsData` from `opponents` (`status == 2` counts as Completed),
`HasPendingRewards` from `waitingForRewards`, and `progressionData` (wins, games,
`ClearedMode`) from the same opponent list. `PvEModeRewardsData.UpdateRewards`
copies `totalRewardSchedule` by loop index, so keys must be `0..n-1` contiguous —
a key set that starts at 1 throws `KeyNotFoundException` and kills the scene.

`TutorialRewardsClaimer.dirtyUpdate` sends `TutorialClaimRewards` as soon as
`HasPendingRewards` is true, so the handshake only happens if the status says a
payout is waiting.

## How this was read

The assembly obfuscates every string literal into a getter in
`<PrivateImplementationDetails>{…}` that slices an XOR-scrambled byte array:

```python
blob[i] = (raw[i] ^ i) ^ 0xAA        # .cctor: for (i = 0; i < arr.Length; i++)
s = blob[offset:offset + length]     # getter: strings[k] ??= GetString(arr, off, len)
```

`~/.capy/work/strs.py` recovers the whole table (~6.2k strings) into
`strs-<assembly>.json`, and `mdump.py` / `find.py` annotate every call to a
getter with its literal — which is how the payload keys (`index`, `subMode`,
`hasAvailableMatches`, `unlock`) and the two message names were read. `find.py`
prints the defining `TypeDef` index for each hit, which is the only way to
address the single-letter obfuscated types reliably.
