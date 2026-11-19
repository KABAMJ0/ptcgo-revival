from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_all_named_then_discard_hand, pokemon_named

card = ItemCardDef(
    guid="b909f055-1be4-5d3c-9e67-d58121a16176",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisLastResort.Name",
    display_name="Giovanni's Last Resort",
    searchable_by=["Giovanni's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=heal_all_named_then_discard_hand(pokemon_named('giovanni'))
)
