from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.card_effects.trainers import choose_condition_attack, discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="be023159-3409-5271-8510-b4324b747af2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaTechnicalMachine01.Name",
    display_name="Team Aqua Technical Machine 01",
    searchable_by=["Team Aqua Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=79,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Miracle",
            game_text="Choose 1 Special Condition. The Defending Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=choose_condition_attack(10),
        ),
        Ability(
            title="Team Aqua Technical Machine 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
)
