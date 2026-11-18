from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_again_chosen, pokemon_named

card = ItemCardDef(
    guid="b06f16a8-994d-527a-81e4-751f8f38f907",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giovanni.Name",
    display_name="Giovanni",
    searchable_by=["Giovanni"],
    subtypes=[],
    collector_number=104,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=evolve_again_chosen(pokemon_named('giovanni'))
)
