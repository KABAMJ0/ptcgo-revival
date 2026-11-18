from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_of_types, takes_less_from

card = StadiumCardDef(
    guid="f23f97e2-ad14-5c48-82f6-a579786983fa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SproutTower.Name",
    display_name="Sprout Tower",
    searchable_by=["Sprout Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(30, None, attacker_of_types('colorless'))
)
