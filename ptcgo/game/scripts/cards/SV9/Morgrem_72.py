from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="651f0013-7191-5f28-86d6-94bf57a41097",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morgrem.Name",
    display_name="Morgrem",
    searchable_by=["Morgrem", "Stage 1", "Morgrem"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Impidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)