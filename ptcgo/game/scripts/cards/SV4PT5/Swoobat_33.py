from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4332a6ef-7ad1-5871-a14d-d8f2e45f3a63",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Attraction Wave",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Put 6 damage counters instead of 3 on that Pok\u00e9mon for this Special Condition.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)