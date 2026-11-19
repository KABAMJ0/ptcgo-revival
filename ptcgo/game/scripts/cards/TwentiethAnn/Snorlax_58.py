from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import sleep_recovery_coins

card = PokemonCardDef(
    guid="a56f6412-3ca1-593d-bc87-c7124f6e01e6",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="TwentiethAnn",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Stir and Snooze",
            game_text="If this Pok\u00e9mon is Asleep, flip 2 coins instead of 1 between turns. If either of them is tails, this Pok\u00e9mon is still Asleep.",
            passive=sleep_recovery_coins(2),
        ),
        Attack(
            title="Sleepy Press",
            game_text="Heal 20 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=unimplemented,
        ),
    ],
)