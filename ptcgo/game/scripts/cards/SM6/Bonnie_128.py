from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import SupporterCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import bonnie, stadium_in_play_playable

card = SupporterCardDef(
    guid="6bdc2fce-76e7-5f93-b359-01371a8198be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    effect=bonnie,
    condition=stadium_in_play_playable,
)
