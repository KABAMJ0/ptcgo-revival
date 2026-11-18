from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="2c3a54c5-e8fa-5994-b0c2-93cfc9d3b592",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiTechnicalMachine01.Name",
    display_name="Multi Technical Machine 01",
    searchable_by=["Multi Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=9,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="The Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
        Ability(
            title="Multi Technical Machine 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
