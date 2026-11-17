from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="dd6dc060-90a6-595d-aa14-12b465e4ddf0",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=opponent_bench_to_active(flip=True)
)
