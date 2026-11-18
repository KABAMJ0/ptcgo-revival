from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69d798ee-18e9-5a32-9a35-57b54df6ba3c",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=35,
    abilities=[
        Attack(
            title="Fairy Power",
            game_text="Return 1 of your Pok\u00e9mon and all cards attached to it in your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Moon Impact",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)