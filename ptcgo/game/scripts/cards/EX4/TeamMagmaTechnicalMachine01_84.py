from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import crushing_magma, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="fe0aa9f0-e8a4-59f6-8566-4911efc060f5",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaTechnicalMachine01.Name",
    display_name="Team Magma Technical Machine 01",
    searchable_by=["Team Magma Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=84,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Crushing Magma",
            game_text="Choose an Energy card attached to the Defending Pokémon and put that card at the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=crushing_magma(10),
        ),
        Ability(
            title="Team Magma Technical Machine 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
