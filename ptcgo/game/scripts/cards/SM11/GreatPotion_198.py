from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_where, is_pokemon_gx

card = ItemCardDef(
    guid="5595381a-0377-5a0c-99aa-3bcec45efb8f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatPotion.Name",
    display_name="Great Potion",
    searchable_by=["Great Potion", "Item"],
    subtypes=["Item"],
    collector_number=198,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=heal_where(50, "active", is_pokemon_gx, min_energy=0)
)
