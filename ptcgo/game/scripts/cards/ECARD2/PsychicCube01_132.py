from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, SpecialConditions, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonToolCardDef(
    guid="864afb6b-aea4-595d-8320-b04e5990d7a5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicCube01.Name",
    display_name="Psychic Cube 01",
    searchable_by=["Psychic Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=132,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Psy Confuse",
            game_text="The Defending Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Ability(
            title="Psychic Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("psychic"),
)
