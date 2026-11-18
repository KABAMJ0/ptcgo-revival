from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81202dc4-d550-5d47-9c6d-47688020b93f",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGengarEX.Name",
    display_name="M Gengar-EX",
    searchable_by=["M Gengar-EX", "MEGA", "EX", "MGengarEX"],
    subtypes=["MEGA", "EX"],
    collector_number=35,
    set_code="XY4",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name",
    family_id=94,
    abilities=[
        Attack(
            title="Phantom Gate",
            game_text="Choose 1 of your opponent's Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)