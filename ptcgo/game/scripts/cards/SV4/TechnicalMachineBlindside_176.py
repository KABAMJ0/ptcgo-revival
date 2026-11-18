from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import blindside, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="1a7325dd-c11d-5260-a965-6aeb1fc35b84",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineBlindside.Name",
    display_name="Technical Machine: Blindside",
    searchable_by=["Technical Machine: Blindside", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=176,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Blindside",
            game_text="This attack does 100 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=blindside(100),
        ),
        Ability(
            title="Technical Machine: Blindside",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
