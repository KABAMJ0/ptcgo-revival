from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_pokemon_card, return_pokemon_to_hand

card = ItemCardDef(
    guid="703ad07f-6dbe-5ffe-9b94-65d390cfb9a0",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpCyclone.Name",
    display_name="Scoop Up Cyclone",
    searchable_by=["Scoop Up Cyclone", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=128,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(predicate=is_pokemon_card)
)
