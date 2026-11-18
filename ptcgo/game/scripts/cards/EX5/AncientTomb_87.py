from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    all_of, any_of, excluding, is_pokemon_ex, is_pokemon_EX,
    stadium_no_weakness,
)


def _has_owner_in_name(card) -> bool:
    """A Pokemon whose printed name carries an owner ("Team Magma's Groudon",
    "Rocket's Scizor", "_____'s Pikachu", "Holon's Electrode")."""
    definition = def_for(card.archetype_id)
    return "'s " in (getattr(definition, "display_name", "") or "")


card = StadiumCardDef(
    guid="c9f6d6ad-d4c9-59d8-b8fc-b8effe6caa69",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTomb.Name",
    display_name="Ancient Tomb",
    searchable_by=["Ancient Tomb", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    passive=stadium_no_weakness(
        all_of(excluding(any_of(is_pokemon_ex, is_pokemon_EX)),
               excluding(_has_owner_in_name))
    ),
)
