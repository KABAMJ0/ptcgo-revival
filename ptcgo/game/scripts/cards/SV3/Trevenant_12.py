from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b875cdf-d0c3-5eab-bb9d-ae1f452fd131",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Ability(
            title="Forest Miasma",
            game_text="During Pok\u00e9mon Checkup, if this Pok\u00e9mon is in the Active Spot, put 1 damage counter on your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Lock Up",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)