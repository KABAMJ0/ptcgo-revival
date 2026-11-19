from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_sleep_attacker

card = PokemonToolCardDef(
    guid="2209d1c7-ba86-550c-9d7d-9630ca3702a2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsHypnotizer.Name",
    display_name="Team Rocket's Hypnotizer",
    searchable_by=["Team Rocket's Hypnotizer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=206,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Team Rocket's Hypnotizer",
            game_text="If the Team Rocket's Pokemon this card is attached to is "
                      "your Active Pokemon and is damaged by an attack from your "
                      "opponent's Pokemon, the Attacking Pokemon is now Asleep.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=tool_sleep_attacker(),
        ),
    ]
)
