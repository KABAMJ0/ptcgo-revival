# League and Gym mode — the client's own response shapes

Read out of the shipped 2020 client assemblies, not guessed: `pie-src.dll`
(metadata tables + `JsonFx.Json.JsonNameAttribute` blobs) and `core.dll` (the
`DwdModelAnalyzer` that drives deserialisation). Scripts that produced this are
listed at the bottom.

## How the client reads a response

- `core.data.JSON.DwdModelAnalyzer` implements JsonFx's `ITokenAnalyzer` and
  registers every `NetworkMessageEvent` subclass by **CLR type name**
  (`RegisterJSONMessage` → `DwdJsonMessages[type.Name] = type`). So the
  `messageName` string is the type name verbatim: `LeagueAndGymModeStatus`,
  `LeagueAndGymModeRewards`, `LeagueAndGymModeError`.
- DTO members are mapped by `JsonFx.Serialization.TypeCoercionUtility.SetMemberValue`,
  i.e. by `[JsonName]` when the member carries one, otherwise by the member name.
  This is why the serverside writes PascalCase members as lowercase keys
  everywhere else (`products`, `items`, `transactionID`) and the client accepts it.
- Obfuscated DTOs (`u.Y`, `u.x`, `u.T`, `A.N`) keep readable wire keys through
  `[JsonName]` attributes, which is what the tables below record.
- Enums are written by name, dictionaries as JSON objects with string keys.

## `LeagueAndGymModeStatus`

Type: `pie.code.pie.gameModules.trainerChallenge.messages.LeagueAndGymModeStatus`
(extends `NetworkMessageEvent`), one member: `status` → `u.Y`.

```
status                      u.Y
├─ opponents                List<u.x>              [JsonName "opponents"]
│  └─ u.x
│     ├─ name               LocalizableText        [JsonName "name"]      → {"id": "<text>"}
│     ├─ image              string                 [JsonName "image"]     → LandingPage-style asset name
│     └─ status             OpponentStatus         [JsonName "status"]    → "Available" | "Unavailable" | "Completed"
├─ playerData               u.T                    [JsonName "playerData"]
│  └─ playerDeckImages      List<string>           [JsonName "playerDeckImages"]
├─ waitingForRewards        bool                   [JsonName "waitingForRewards"]
└─ losses                   int                    [JsonName "losses"]
```

Empty state (no leagues, no opponents, nothing waiting):

```json
{
  "messageName": "LeagueAndGymModeStatus",
  "status": {
    "opponents": [],
    "playerData": { "playerDeckImages": [] },
    "waitingForRewards": false,
    "losses": 0
  }
}
```

With one opponent, for reference:

```json
{
  "messageName": "LeagueAndGymModeStatus",
  "status": {
    "opponents": [
      {
        "name": { "id": "Zach" },
        "image": "zach_landingpage",
        "status": "Available"
      }
    ],
    "playerData": { "playerDeckImages": ["Basic_Green_Deck"] },
    "waitingForRewards": false,
    "losses": 2
  }
}
```

`OpponentStatus` values, in metadata order: `Available`, `Unavailable`,
`Completed` (an ordinary `System.Enum`, so the name string is what JsonFx emits).

## `LeagueAndGymModeRewards`

Type: `pie.code.pie.gameModules.trainerChallenge.messages.LeagueAndGymModeRewards`,
one member: `totalRewardSchedule` → `Dictionary<int, List<A.N>>` — league (or
tier) id → its reward entries.

`A.N` (a plain `System.Object` subclass, one member) is the client's generic
reward item, also used by daily rewards and versus season rewards:

```
A.N
└─ A                      dwd.legacy.CurrencyAmount   (no [JsonName] — see caveat)
   └─ amount              P.u                     [JsonName "amount"]
      ├─ name             int                     [JsonName "name"]   → currency id
      └─ value            int                     [JsonName "value"]  → amount
```

Empty state:

```json
{ "messageName": "LeagueAndGymModeRewards", "totalRewardSchedule": {} }
```

**Confirmed on the wire, 2026-11-18.** The map is indexed 0..Count-1: the client's
`PvEModeRewardsData.UpdateRewards` copies it into its own array with
`for (i = 0; i < map.Count; i++) array[i] = map[i]`, so a schedule keyed from 1
throws `KeyNotFoundException` ("The given key was not present in the dictionary")
the moment rewards arrive, and the trainer challenge scene dies. Keys must be
`"0"`, `"1"`, `"2"`… contiguous from zero. The `A` wrapper key is accepted as
written.

A populated schedule would therefore be (caveat below):

```json
{
  "messageName": "LeagueAndGymModeRewards",
  "totalRewardSchedule": {
    "1": [ { "A": { "amount": { "name": 0, "value": 25 } } } ]
  }
}
```

**Caveat on the reward item key.** `A.N`'s single member is named `A` in
metadata and carries *no* `[JsonName]`, so JsonFx's rule says the key is `A`.
Every other DTO in this path has a readable `[JsonName]`, so this one looks like
an obfuscation leftover. It does not matter for the empty state — send
`"totalRewardSchedule": {}` and no item shapes are involved. When rewards are
actually needed, confirm the key once on the wire (ask the client to render one
item and watch whether it accepts `A` or `amount`); the wrapper's shape is
certain, only its key name is.

## `LeagueAndGymModeError`

Type: `...trainerChallenge.messages.LeagueAndGymModeError`, one member
`Message` → `dwd.core.localization.LocalizableText`, `[JsonName "msg"]`:

```json
{ "messageName": "LeagueAndGymModeError", "msg": { "id": "league.error.unavailable" } }
```

## What the current handler does

`ptcgo/packets/handlers/league.py` answers both requests with `{}`. That
completes the RPC (the spinner stops) and leaves the scene with no state, which
is why the tab renders blank. The two skeletons above are the smallest payloads
that give the client an empty-but-valid league state; nothing else in
`LeagueAndGymMode*` needs to be sent.

## How these were read

- `python <venv> mddump.py "…/pie-src.dll" LeagueAndGymMode` — TypeDef → members
  with CLR types parsed from the signature blobs.
- Field/type-level `[JsonName]` values decoded from the `CustomAttribute` table
  (`JsonFx.Json.JsonNameAttribute`, ctor token resolved through `TypeRef 45`).
- `DwdModelAnalyzer.RegisterJSONMessage` / `ConsumeObject` disassembled with
  `dncil` to confirm the reader keys messages by type name and delegates member
  mapping to JsonFx (`TypeCoercionUtility.SetMemberValue`).
- `A.N` consumers found by token reference: versus, daily and end-of-game reward
  renderers all read `A.N::A`, i.e. it really is the shared reward item type.

Helper scripts used, not committed: `mddump.py` (TypeDef/field/property dump),
`attrs.py` (JsonName decode), `il.py` (one method disassembly), `refscan.py`
(methods referencing a member). They run on the repo venv, which has `dnfile`
and `dncil` installed.
