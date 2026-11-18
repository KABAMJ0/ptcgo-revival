from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="06d39a2d-6b7a-5be0-baac-0364c88ebe07",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
