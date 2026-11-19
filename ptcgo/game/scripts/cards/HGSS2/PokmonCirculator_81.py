from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="b083dacb-0e95-5a16-b847-f8dcc549d6f3",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCirculator.Name",
    display_name="Pokémon Circulator",
    searchable_by=["Pok\u00e9mon Circulator", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
