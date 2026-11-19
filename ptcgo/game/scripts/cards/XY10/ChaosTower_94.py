from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.passives_common import condition_immunity_passive

card = StadiumCardDef(
    guid="b261ac6f-3f12-5fb5-ac4d-21f93dfe979d",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaosTower.Name",
    display_name="Chaos Tower",
    searchable_by=["Chaos Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    faces={
        "confused-poisoned": {"passive": condition_immunity_passive(
            (SpecialConditions.CONFUSED, SpecialConditions.POISONED),
            protects="team")},
        "asleep-paralyzed": {"passive": condition_immunity_passive(
            (SpecialConditions.ASLEEP, SpecialConditions.PARALYZED),
            protects="team")},
    },
    face_labels={
        "confused-poisoned": "This side can't be Confused or Poisoned",
        "asleep-paralyzed": "This side can't be Asleep or Paralyzed",
    },
)
