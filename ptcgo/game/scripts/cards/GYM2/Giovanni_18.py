from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_again_chosen, pokemon_named

card = ItemCardDef(
    guid="43919234-6fbb-5ffa-b663-001b09ab8cd4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giovanni.Name",
    display_name="Giovanni",
    searchable_by=["Giovanni"],
    subtypes=[],
    collector_number=18,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    effect=evolve_again_chosen(pokemon_named('giovanni'))
)
