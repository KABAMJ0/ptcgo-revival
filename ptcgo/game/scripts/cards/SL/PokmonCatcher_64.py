from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="ff13f3cf-5e8c-58d0-baf5-683ab296b524",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="SL",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(flip=True)
)
