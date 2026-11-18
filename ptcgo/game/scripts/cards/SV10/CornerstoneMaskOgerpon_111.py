from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4cd26fdb-7421-554e-869f-2342e5cc99e1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerpon.Name",
    display_name="Cornerstone Mask Ogerpon",
    searchable_by=["Cornerstone Mask Ogerpon", "Basic", "CornerstoneMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1017,
    abilities=[
        Attack(
            title="Rock Kagura",
            game_text="Search your deck for a Basic Fighting Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)