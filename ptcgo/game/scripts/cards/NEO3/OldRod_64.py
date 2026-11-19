from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_both_recover, is_pokemon_card, is_trainer_card

card = ItemCardDef(
    guid="1d88c3b4-8160-5e7b-9a57-21c661c71984",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod"],
    subtypes=[],
    collector_number=64,
    set_code="NEO3",
    rarity=Rarities.Common,
    effect=flip_both_recover(is_pokemon_card, is_trainer_card)
)
