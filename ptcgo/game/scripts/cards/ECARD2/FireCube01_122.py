from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, SpecialConditions, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonToolCardDef(
    guid="61024ef9-d0d7-542b-8ef8-041f77f2d6da",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCube01.Name",
    display_name="Fire Cube 01",
    searchable_by=["Fire Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=122,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Singe",
            game_text="The Defending Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Ability(
            title="Fire Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("fire"),
)
