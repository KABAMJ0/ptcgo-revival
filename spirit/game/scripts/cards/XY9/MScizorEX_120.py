from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7f940ad9-d5e3-58f1-bb80-d2c871785c37",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MScizorEX.Name",
    display_name="M Scizor-EX",
    searchable_by=["M Scizor-EX", "MEGA", "EX", "MScizorEX"],
    subtypes=["MEGA", "EX"],
    collector_number=120,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name",
    family_id=212,
    abilities=[
        Attack(
            title="Iron Crusher",
            game_text="You may discard a Special Energy attached to your opponent's Active Pok\u00e9mon or a Stadium card in play.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)