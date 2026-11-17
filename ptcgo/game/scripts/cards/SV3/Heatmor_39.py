from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="616948ff-a044-59c6-a852-7bcb63a58842",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Energy Burner",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)