from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_typed_pokemon_to_bench_then_draw, hand_is_last

card = SupporterCardDef(
    guid="813bc3c3-c4b3-5915-a681-4a028bdc14e3",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name",
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", "Supporter"],
    subtypes=["Supporter"],
    collector_number=158,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=discard_typed_pokemon_to_bench_then_draw("fighting", 5), condition=hand_is_last()
)
