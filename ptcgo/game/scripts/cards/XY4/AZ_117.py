from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = SupporterCardDef(
    guid="bb3855cc-0a1e-5265-adc3-428851559235",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZ.Name",
    display_name="AZ",
    searchable_by=["AZ", "Supporter"],
    subtypes=["Supporter"],
    collector_number=117,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    effect=return_pokemon_to_hand(with_attachments="discard")
)
