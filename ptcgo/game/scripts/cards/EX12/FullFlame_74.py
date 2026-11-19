from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import full_flame

card = StadiumCardDef(
    guid="1abc2770-40e4-51f1-8771-3bb5b86b271d",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullFlame.Name",
    display_name="Full Flame",
    searchable_by=["Full Flame", "Stadium"],
    subtypes=["Stadium"],
    collector_number=74,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    effect=full_flame()
)
