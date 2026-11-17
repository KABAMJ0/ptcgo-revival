from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="507be899-1331-54bd-9410-6178f0b8df0f",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
