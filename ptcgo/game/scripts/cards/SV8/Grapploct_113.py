from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ddc34dc-bc1d-5b83-ba76-df3d6d543d75",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1", "Grapploct"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Chop",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Raging Tentacles",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack can be used for Fighting.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)