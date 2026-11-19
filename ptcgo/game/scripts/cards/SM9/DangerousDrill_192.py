from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_opponent_attachment_or_stadium, hand_has, pokemon_of

card = ItemCardDef(
    guid="e2576c95-282f-5b91-abb8-dbae0cc31809",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=discard_opponent_attachment_or_stadium(pokemon_of("darkness"), "a Darkness Pokemon"),
    condition=hand_has(pokemon_of("darkness"), 1)
)
