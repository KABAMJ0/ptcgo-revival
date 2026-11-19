from ptcgo.game.data_utils import StadiumCardDef, evolves_from
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import ends_turn_after, stadium_ability
from ptcgo.game.card_effects.support_common import search_to_bench


def _evolves_from_unidentified_fossil(card) -> bool:
    """A Pokemon that evolves from Unidentified Fossil."""
    return evolves_from(getattr(card, "archetype_id", None), "UnidentifiedFossil")

_SEARCH_FOSSIL_EVOLUTIONS = ends_turn_after(search_to_bench(
    _evolves_from_unidentified_fossil, count=2,
    prompt="Choose up to 2 Pok\u00e9mon that evolve from Unidentified Fossil "
           "for your Bench"))


card = StadiumCardDef(
    guid="1a8505d9-1d49-5ac0-b6f2-167cf497904d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonResearchLab.Name",
    display_name="Pokémon Research Lab",
    searchable_by=["Pok\u00e9mon Research Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Pok\u00e9mon Research Lab",
                            _SEARCH_FOSSIL_EVOLUTIONS),
)
