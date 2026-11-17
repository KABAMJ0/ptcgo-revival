from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e650d4fa-c155-57ce-b64a-7fe37ba9d86f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    display_name="Pignite",
    searchable_by=["Pignite", "Stage 1", "Pignite"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Heat Crash",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)