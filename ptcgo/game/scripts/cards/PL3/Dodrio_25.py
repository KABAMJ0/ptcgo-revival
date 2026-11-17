from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="27831926-8f19-5d66-a030-b2494a5df40f",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Ability(
            title="Echo Draw",
            game_text="Once during your turn (before your attack), you may draw a card. This power can't be used if Dodrio is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Drill Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)