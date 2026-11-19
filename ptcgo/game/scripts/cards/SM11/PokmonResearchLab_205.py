from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import (
    ends_turn_after, stadium_ability,
)


def _evolves_from_unidentified_fossil(card) -> bool:
    """A Pokemon whose direct pre-evolution is Unidentified Fossil.

    Reads EVOLUTION_LOGIC_FROM (the pre-evolution's logic name).
    `trainers.fossil_evolution_card` reads EVOLUTION_LOGIC_NAME -- the card's
    own name -- which no fossil evolver carries, so it matches nothing.
    """
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == "UnidentifiedFossil"


_SEARCH = ends_turn_after(search_to_bench(_evolves_from_unidentified_fossil, 2))


card = StadiumCardDef(
    guid="1a8505d9-1d49-5ac0-b6f2-167cf497904d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonResearchLab.Name",
    display_name="Pok\u00e9mon Research Lab",
    searchable_by=["Pok\u00e9mon Research Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=stadium_ability(
        "Pok\u00e9mon Research Lab", _SEARCH),
)
