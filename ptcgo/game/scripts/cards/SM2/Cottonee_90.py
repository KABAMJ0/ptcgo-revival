from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ebeace2-f3e8-5409-b3bd-fd3d50c76d9d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic", "Cottonee"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=546,
    abilities=[
        Attack(
            title="Continuous Tumble",
            game_text="Flip a coin until you get tails. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)