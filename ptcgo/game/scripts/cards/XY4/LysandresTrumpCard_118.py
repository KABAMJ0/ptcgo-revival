from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_discard_into_deck

card = SupporterCardDef(
    guid="dafac91a-ca68-5667-8a1f-f518503823e8",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandresTrumpCard.Name",
    display_name="Lysandre's Trump Card",
    searchable_by=["Lysandre's Trump Card", "Supporter"],
    subtypes=["Supporter"],
    collector_number=118,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    effect=each_player_shuffle_discard_into_deck()
)
