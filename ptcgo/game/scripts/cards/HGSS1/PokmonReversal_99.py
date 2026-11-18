from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="4eef2063-1115-58f7-932d-836a9e398199",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(flip=True)
)
