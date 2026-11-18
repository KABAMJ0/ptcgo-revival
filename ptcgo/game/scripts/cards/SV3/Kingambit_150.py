from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58f46713-7c66-52ad-9049-0496e2899cab",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingambit.Name",
    display_name="Kingambit",
    searchable_by=["Kingambit", "Stage 2", "Kingambit"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Strike Down",
            game_text="If your opponent's Active Pok\u00e9mon has 4 or more damage counters on it, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Massive Rend",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)