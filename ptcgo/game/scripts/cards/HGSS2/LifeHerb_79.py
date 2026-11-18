from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_heal_cure, is_pokemon_card

card = ItemCardDef(
    guid="9ff543bc-dc73-5725-ac8e-150791e49c25",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=flip_heal_cure(is_pokemon_card, 60, 1)
)
