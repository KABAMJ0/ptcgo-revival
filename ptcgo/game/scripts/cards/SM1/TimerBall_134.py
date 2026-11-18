from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_per_head, is_evolution_pokemon

card = ItemCardDef(
    guid="4b3ceeb2-1e9f-50b9-b82f-7a3c962117a3",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimerBall.Name",
    display_name="Timer Ball",
    searchable_by=["Timer Ball", "Item"],
    subtypes=["Item"],
    collector_number=134,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=flip_search_per_head(2, is_evolution_pokemon, 1)
)
