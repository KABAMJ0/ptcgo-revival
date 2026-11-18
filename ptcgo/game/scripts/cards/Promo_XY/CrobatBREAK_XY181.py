from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f80fe6e-99a8-5010-8d40-4df848a9b7c6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatBREAK.Name",
    display_name="Crobat BREAK",
    searchable_by=["Crobat BREAK", "BREAK", "CrobatBREAK"],
    subtypes=["BREAK"],
    collector_number=181,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Silent Bite",
            game_text="You may leave your opponent's Active Pok\u00e9mon Paralyzed. If you do, shuffle this Pok\u00e9mon and all cards attached to into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)