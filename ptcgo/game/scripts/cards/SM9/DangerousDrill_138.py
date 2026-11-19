from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_attachment_or_stadium, hand_has, pokemon_of

card = ItemCardDef(
    guid="d1f44010-4fbc-5195-be78-de8b65fb1949",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=discard_opponent_attachment_or_stadium(pokemon_of("darkness"), "a Darkness Pokemon"),
    condition=hand_has(pokemon_of("darkness"), 1)
)
