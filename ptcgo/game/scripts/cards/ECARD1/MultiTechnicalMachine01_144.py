from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn

card = PokemonToolCardDef(
    guid="66be2075-cf24-5927-8a3c-4417587c8c4c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiTechnicalMachine01.Name",
    display_name="Multi Technical Machine 01",
    searchable_by=["Multi Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=144,
    set_code="ECARD1",
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
