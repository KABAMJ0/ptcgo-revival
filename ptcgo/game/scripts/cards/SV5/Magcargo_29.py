from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42d21503-037e-5882-9044-488f8d35f96f",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Lava Zone",
            game_text="Whenever your opponent's Active Pok\u00e9mon moves to the Bench during their turn, their new Active Pok\u00e9mon is now Burned.",
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)