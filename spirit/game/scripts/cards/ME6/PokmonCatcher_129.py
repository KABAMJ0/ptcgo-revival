from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="89ab3190-09fc-5c8d-b62e-c630ec13da46",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="ME6",
    rarity=Rarities.Rare,
    effect=opponent_bench_to_active(flip=True)
)
