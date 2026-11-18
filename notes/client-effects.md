# Client effect payloads

Types carrying `[DwdJsonEffect]`: they are serialised inside game messages (entity moves, attack effects, data carriers), so their keys have to match exactly as well. Shapes are rendered the same way as `client-protocol.md`.

- effect types: **44**

## AbilityFinishedEffect

```json
{
  "eID": <dwd.core.match.EntityID>
}
```

## AbilityPlayedEffect

```json
{
  "eID": <dwd.core.match.EntityID>,
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
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>]
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
  "entityID": <dwd.core.match.EntityID>,
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
  "damageSource": <dwd.core.match.EntityID>,
  "entityID": <dwd.core.match.EntityID>,
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
  "entityID": <dwd.core.match.EntityID>,
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
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>],
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
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>]
}
```

## GXAttackUsedEffect

```json
{
  "user": <dwd.core.account.AccountID>
}
```

## HealWithContextEvent

```json
{
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>]
}
```

## MulliganRevealCardsEffect

```json
{
  "player": <dwd.core.account.AccountID>,
  "entityIDPiles": [
    {
      "<dwd.core.match.EntityID key>": {
        "source": {
          "globalDefaults": <dwd.core.attributes.AttributeDictionary>,
          "data": <dwd.core.attributes.AttributeDictionary>,
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
  "revealSource": <dwd.core.match.EntityID>
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
  "source": <dwd.core.match.EntityID>
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
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>],
  "gameText": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## NonDamagingTargetsEffect

```json
{
  "targets": [<dwd.core.match.EntityID>]
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
  "destinationID": <dwd.core.match.EntityID>,
  "originID": <dwd.core.match.EntityID>,
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
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>]
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
  "entityID": [<dwd.core.match.EntityID>],
  "playerPrompt": {
    "<dwd.core.account.AccountID key>": {
      "trimChars": [<char>],
      "id": <string>
    }
  },
  "revealTitle": {
    "trimChars": [<char>],
    "id": <string>
  },
  "revealSource": <dwd.core.match.EntityID>,
  "prompt": {
    "trimChars": [<char>],
    "id": <string>
  }
}
```

## RevealCardsToPlayerEffect

```json
{
  "player": <dwd.core.account.AccountID>,
  "entityID": [<dwd.core.match.EntityID>],
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
  "revealSource": <dwd.core.match.EntityID>
}
```

## RockPaperScissorsEffect

```json
{
  "choices": {
    "<dwd.core.account.AccountID key>": <int>
  }
}
```

## ShieldTargetsEffect

```json
{
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>],
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
  "attackerID": <dwd.core.match.EntityID>,
  "defenderID": <dwd.core.match.EntityID>,
  "effectType": <string>
}
```

## ClearAttackEffect

```json
{
  "attackerID": <dwd.core.match.EntityID>,
  "defenderList": [<dwd.core.match.EntityID>],
  "effectType": <string>
}
```

## SwapAttackerEffect

```json
{
  "oldAttackerID": <dwd.core.match.EntityID>,
  "newAttackerID": <dwd.core.match.EntityID>
}
```

## EnergySwapEffect

```json
{
  "source": <dwd.core.match.EntityID>,
  "targets": [<dwd.core.match.EntityID>]
}
```

## DrawFromBottom

```json
{
  "playerID": <dwd.core.match.EntityID>,
  "numOfTargets": <int>
}
```

## PlaceOnBottom

```json
{
  "entityID": <dwd.core.match.EntityID>,
  "target": <dwd.core.match.EntityID>
}
```

