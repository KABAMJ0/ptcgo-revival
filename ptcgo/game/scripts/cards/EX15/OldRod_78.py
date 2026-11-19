from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_both_recover, is_pokemon_card, is_trainer_card

card = ItemCardDef(
    guid="31ad4660-f40b-5c53-bace-f47b33c8155c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OldRod.Name",
    display_name="Old Rod",
    searchable_by=["Old Rod", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=flip_both_recover(is_pokemon_card, is_trainer_card)
)
