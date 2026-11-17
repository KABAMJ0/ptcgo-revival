from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="246f0f8d-c3ee-53d8-941a-084dbe51bbd5",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy Paunch",
            game_text="If Slaking used any attacks during your last turn, Slaking can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Best Dash",
            game_text="During your opponent's next turn, any damage done to Slaking by attacks is increased by 50 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=unimplemented,
        ),
    ],
)