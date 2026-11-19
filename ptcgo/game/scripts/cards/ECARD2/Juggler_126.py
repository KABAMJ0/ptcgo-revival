from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_up_to_draw_pair, is_basic_energy_card

card = SupporterCardDef(
    guid="7c18debc-aa03-5c09-bcbc-d2590b55bd96",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Juggler.Name",
    display_name="Juggler",
    searchable_by=["Juggler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=discard_up_to_draw_pair(2, is_basic_energy_card, 3, 5)
)
