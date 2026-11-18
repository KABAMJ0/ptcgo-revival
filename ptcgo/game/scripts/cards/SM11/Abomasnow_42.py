from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95480d40-7a87-5e2d-a2fe-e0649b3f2fe2",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Quick Freeze",
            game_text="If your opponent's Active Pok\u00e9mon has any Water Energy attached to it, it is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)