from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card, return_pokemon_to_hand

card = ItemCardDef(
    guid="9198960d-2e12-5ee4-bbb3-b96d8949f249",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpCyclone.Name",
    display_name="Scoop Up Cyclone",
    searchable_by=["Scoop Up Cyclone", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=162,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(predicate=is_pokemon_card)
)
