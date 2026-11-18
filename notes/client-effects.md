# Client effect payloads

Types carrying `[DwdJsonEffect]`: they are serialised inside game messages (entity moves, attack effects, data carriers), so their keys have to match exactly as well. Shapes are rendered the same way as `client-protocol.md`.

- effect types: **44**

## AbilityFinishedEffect

```json
{
  "eID": <Guid>
}
```

## AbilityPlayedEffect

```json
{
  "eID": <Guid>,
  "abilityID": <System.Guid>,
  "abilityTitle": {
    "trimChars": [<char>],
    "id": <string>
  },
  "abilityType": "ALL | Attack | PokeAbility | Retreats | Stadium | UndoAction"
}
```

## AddSpecialConditionEffect

```json
{
  "condition": "Asleep | Burned | Confused | Paralyzed | Poisoned | UNSET",
  "source": <Guid>,
  "targets": [<Guid>]
}
```

## BurnEffect

```json
{

}
```

## CakeAbilitySelectedEffect

```json
{
  "entityID": <Guid>,
  "abilityName": {
    "trimChars": [<char>],
    "id": <string>
  },
  "abilityType": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## CakeAttackEffect

```json
{
  "damageSource": <Guid>,
  "entityID": <Guid>,
  "weaknessTriggered": <bool>,
  "resistanceTrigger": <bool>,
  "damageType": [<string>],
  "attackName": {
    "trimChars": [<char>],
    "id": <string>
  },
  "damageAmount": <int>,
  "damageModification": <int>,
  "visualType": "DamagingAction | NonDamagingAction"
}
```

## CleanupAttackEffect

```json
{
  "entityID": <Guid>,
  "cleanupCurvePrefix": <string>
}
```

## ClosePauseOnPromptEffect

```json
{

}
```

## ConfuseEffect

```json
{

}
```

## CreatureHealEvent

```json
{

}
```

## CreatureHealWithContextEvent

```json
{
  "source": <Guid>,
  "targets": [<Guid>],
  "amount": <int>
}
```

## DoneWaitingForOpponentEffect

```json
{

}
```

## EvolveEffect

```json
{

}
```

## EvolveWithContextEffect

```json
{
  "source": <Guid>,
  "targets": [<Guid>]
}
```

## GXAttackUsedEffect

```json
{
  "user": <Guid>
}
```

## HealWithContextEvent

```json
{
  "source": <Guid>,
  "targets": [<Guid>]
}
```

## MulliganRevealCardsEffect

```json
{
  "player": <Guid>,
  "entityIDPiles": [
    {
      "<Guid key>": {
        "source": {
          "globalDefaults": {
            "<string key>": null
          },
          "data": {
            "<string key>": null
          },
          "useGlobalDefaults": <bool>
        }
      }
    }
  ],
  "prompt": {
    "trimChars": [<char>],
    "id": <string>
  },
  "revealTitle": {
    "trimChars": [<char>],
    "id": <string>
  },
  "revealSource": <Guid>
}
```

## MultipleCoinFlipEffect

```json
{
  "resultLst": [<int>],
  "title": {
    "trimChars": [<char>],
    "id": <string>
  },
  "gameText": {
    "trimChars": [<char>],
    "id": <string>
  },
  "source": <Guid>
}
```

## MultipleCoinFlipWithContextEffect

```json
{
  "resultLst": [<int>],
  "title": {
    "trimChars": [<char>],
    "id": <string>
  },
  "source": <Guid>,
  "targets": [<Guid>],
  "gameText": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## NonDamagingTargetsEffect

```json
{
  "targets": [<Guid>]
}
```

## ParalyzeEffect

```json
{

}
```

## PauseOnPromptEffect

```json
{
  "buttonText": {
    "trimChars": [<char>],
    "id": <string>
  },
  "prompt": {
    "textVars": {
      "numberMap": {
        "<string key>": <int>
      },
      "stringMap": {
        "<string key>": <string>
      },
      "varMap": {
        "<string key>": <object>
      }
    }
  },
  "doPause": <bool>
}
```

## PlaceDamageEffect

```json
{
  "destinationID": <Guid>,
  "originID": <Guid>,
  "amount": <int>,
  "abilityName": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## PoisonEffect

```json
{

}
```

## PostActionPhaseEffect

```json
{

}
```

## RemoveBurnEffect

```json
{

}
```

## RemoveConfuseEffect

```json
{

}
```

## RemoveParalyzeEffect

```json
{

}
```

## RemovePoisonEffect

```json
{

}
```

## RemoveSleepEffect

```json
{

}
```

## RemoveSpecialConditionEffect

```json
{
  "condition": "Asleep | Burned | Confused | Paralyzed | Poisoned | UNSET",
  "source": <Guid>,
  "targets": [<Guid>]
}
```

## RevealCardToAllEffect

```json
{
  "entityID": <System.Guid>,
  "Return": <bool>,
  "alwaysReveal": <bool>
}
```

## RevealCardsToAllEffect

```json
{
  "entityID": [<Guid>],
  "playerPrompt": {
    "<Guid key>": {
      "trimChars": [<char>],
      "id": <string>
    }
  },
  "revealTitle": {
    "trimChars": [<char>],
    "id": <string>
  },
  "revealSource": <Guid>,
  "prompt": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## RevealCardsToPlayerEffect

```json
{
  "player": <Guid>,
  "entityID": [<Guid>],
  "prompt": {
    "textVars": {
      "numberMap": {
        "<string key>": <int>
      },
      "stringMap": {
        "<string key>": <string>
      },
      "varMap": {
        "<string key>": <object>
      }
    }
  },
  "revealTitle": {
    "trimChars": [<char>],
    "id": <string>
  },
  "revealSource": <Guid>
}
```

## RockPaperScissorsEffect

```json
{
  "choices": {
    "<Guid key>": <int>
  }
}
```

## ShieldTargetsEffect

```json
{
  "source": <Guid>,
  "targets": [<Guid>],
  "wasDamage": <bool>
}
```

## SleepEffect

```json
{

}
```

## WaitingForOpponentEffect

```json
{
  "message": <string>,
  "maxTimeToWait": <int>,
  "selectingAccountID": <System.Guid>
}
```

## AttackEffect

```json
{
  "attackerID": <Guid>,
  "defenderID": <Guid>,
  "effectType": <string>
}
```

## ClearAttackEffect

```json
{
  "attackerID": <Guid>,
  "defenderList": [<Guid>],
  "effectType": <string>
}
```

## SwapAttackerEffect

```json
{
  "oldAttackerID": <Guid>,
  "newAttackerID": <Guid>
}
```

## EnergySwapEffect

```json
{
  "source": <Guid>,
  "targets": [<Guid>]
}
```

## DrawFromBottom

```json
{
  "playerID": <Guid>,
  "numOfTargets": <int>
}
```

## PlaceOnBottom

```json
{
  "entityID": <Guid>,
  "target": <Guid>
}
```

