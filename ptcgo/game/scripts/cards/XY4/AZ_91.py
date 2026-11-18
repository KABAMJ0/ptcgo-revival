from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import return_pokemon_to_hand

card = SupporterCardDef(
    guid="19230d7c-22ec-5261-baae-817ebad18999",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZ.Name",
    display_name="AZ",
    searchable_by=["AZ", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(with_attachments="discard")
)
