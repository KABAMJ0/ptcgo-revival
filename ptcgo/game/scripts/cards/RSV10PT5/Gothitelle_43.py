from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af3a7665-6475-5e0b-b0cc-669486a52281",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothitelle.Name",
    display_name="Gothitelle",
    searchable_by=["Gothitelle", "Stage 2", "Gothitelle"],
    subtypes=["Stage 2"],
    collector_number=43,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    family_id=574,
    abilities=[
        Ability(
            title="Distorted Future",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may have your opponent shuffle their hand into their deck and draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Shot",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)