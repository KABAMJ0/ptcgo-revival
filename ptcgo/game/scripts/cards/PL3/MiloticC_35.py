from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="6fc83a2e-be82-57c3-88ad-52001549f03e",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MiloticC.Name",
    display_name="Milotic C",
    searchable_by=["Milotic C", "Basic", "SP", "MiloticC"],
    subtypes=["Basic", "SP"],
    collector_number=35,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=350,
    abilities=[
        Attack(
            title="Aqua Tail",
            game_text="Flip a coin for each Water Energy attached to Milotic C. This attack does 10 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Wrap",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)