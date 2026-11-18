from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="53921195-6aad-521d-ad1d-645be1d0cc67",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=111,
    set_code="BW5",
    rarity=Rarities.RareSecret,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
