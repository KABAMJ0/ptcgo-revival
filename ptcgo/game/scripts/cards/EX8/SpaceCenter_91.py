from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    abilities_off_for, is_pokemon_EX, is_pokemon_ex,
)
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.effects import is_basic_pokemon


def _has_owner_in_name(card):
    name = (getattr(def_for(card.archetype_id), "display_name", "") or "")
    return "'s " in name.replace("\u2019", "'")


def _ignores_bodies(card):
    return is_basic_pokemon(card) and not (is_pokemon_ex(card) or is_pokemon_EX(card)) \
        and not _has_owner_in_name(card)


card = StadiumCardDef(
    guid="f4f6c5fa-54c9-547d-a81e-dad8f2747207",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpaceCenter.Name",
    display_name="Space Center",
    searchable_by=["Space Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(_ignores_bodies),
)
