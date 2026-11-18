from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="f97bcd3a-7386-5f0e-a5c4-3cb20f8c858c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal"],
    subtypes=[],
    collector_number=146,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(flip=True)
)
