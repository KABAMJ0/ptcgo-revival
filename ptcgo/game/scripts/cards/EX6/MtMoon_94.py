from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities, AttrID
from ptcgo.game.card_effects.trainers import abilities_off_for


def _printed_max_hp_at_most(limit):
    """A Pokemon whose PRINTED maximum HP is `limit` or less.

    The passive hook is `blocks_abilities(pokemon, carrier)` and carries no
    board, so this reads the definition rather than the live max HP
    (`session/passives.py:347`); a +HP stadium or tool is not added in.
    """
    def predicate(pokemon):
        definition = def_for(pokemon.archetype_id)
        spec = definition.extra_attributes.get(str(AttrID.HP.value)) or {}
        return (spec.get("value") or 0) <= limit
    return predicate

card = StadiumCardDef(
    guid="71fb1a9d-63cb-5cee-af3c-cc7c8202a493",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtMoon.Name",
    display_name="Mt. Moon",
    searchable_by=["Mt. Moon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(_printed_max_hp_at_most(70))
)
