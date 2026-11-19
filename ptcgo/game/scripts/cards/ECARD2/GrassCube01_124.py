from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities, SpecialConditions, PokemonTypes
from ptcgo.game.card_effects.trainers import discard_tool_at_end_of_turn, pokemon_of
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonToolCardDef(
    guid="a7ab2f81-e315-5718-8609-c1b3d67d6e68",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrassCube01.Name",
    display_name="Grass Cube 01",
    searchable_by=["Grass Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=124,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Sleep Poison",
            game_text="The Defending Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP,
                                    SpecialConditions.POISONED),
        ),
        Ability(
            title="Grass Cube 01",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=pokemon_of("grass"),
)
