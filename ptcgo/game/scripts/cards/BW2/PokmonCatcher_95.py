from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="0a553e6a-00d3-5d43-b06f-bd4871199325",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
