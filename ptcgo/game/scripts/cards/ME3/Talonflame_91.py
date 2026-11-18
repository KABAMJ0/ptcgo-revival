from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d3fabdf4-5246-50e3-b926-531f5d445eae",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=91,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Sky Hunt",
            game_text="Once during your turn, you may use this Ability. Flip a coin. If heads, discard a random card from your opponent's hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2},
            damage=110,
        ),
    ],
)