from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="bfe85cc5-5c11-59f5-acd3-49fb1b3caeeb",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regice.Name",
    display_name="Regice",
    searchable_by=["Regice", "Basic", "Regice"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="EX13",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=378,
    abilities=[
        Ability(
            title="Clear Body",
            game_text="Regice can't be affected by any Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Icy Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)