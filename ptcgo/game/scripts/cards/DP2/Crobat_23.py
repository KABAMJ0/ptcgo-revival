from ptcgo.game.card_effects.attacks_common import poison_defender_on_evolve
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edb5a67e-62b5-5b21-ace1-28823e2c7173",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="DP2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Evolutionary Toxic",
            game_text="Once during your turn, when you play Crobat from your hand to evolve 1 of your Pok\u00e9mon, you may choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            effect=poison_defender_on_evolve(2),
        ),
        Attack(
            title="Strike and Fade",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 50 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Flip a coin. If tails, shuffle Crobat and all cards attached to it back into your deck.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
    ],
)
