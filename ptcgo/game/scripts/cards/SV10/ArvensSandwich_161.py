from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_active_or, pokemon_named

card = ItemCardDef(
    guid="bae4ddf4-97b5-5022-a9ae-11c207d6ebe5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArvensSandwich.Name",
    display_name="Arven's Sandwich",
    searchable_by=["Arven's Sandwich", "Item"],
    subtypes=["Item"],
    collector_number=161,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=heal_active_or(pokemon_named("arvens"), 30, 100)
)
