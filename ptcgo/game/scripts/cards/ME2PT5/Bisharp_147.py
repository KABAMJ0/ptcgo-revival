from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ccb40ef-2095-5d18-968d-c35ff227248a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1", "Bisharp"],
    subtypes=["Stage 1"],
    collector_number=147,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Rapid Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)