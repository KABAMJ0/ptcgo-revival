from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_both_search_attach, is_basic_energy_card

card = ItemCardDef(
    guid="0f6e5cd3-8943-5782-9a16-e95168fca714",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCoin.Name",
    display_name="Energy Coin",
    searchable_by=["Energy Coin", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    effect=flip_both_search_attach(is_basic_energy_card, 2)
)
