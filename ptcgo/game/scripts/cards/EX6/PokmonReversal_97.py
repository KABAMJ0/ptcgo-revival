from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="f50778a1-64a5-5fbf-bf3e-c5ee99a6f53d",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(flip=True)
)
