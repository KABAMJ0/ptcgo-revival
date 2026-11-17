from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_typed_pokemon_to_bench_then_draw, hand_is_last

card = SupporterCardDef(
    guid="efa04d27-1a71-5a98-a0d9-d7a99c2c6795",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxiesHiddenBallTrick.Name",
    display_name="Maxie's Hidden Ball Trick",
    searchable_by=["Maxie's Hidden Ball Trick", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=discard_typed_pokemon_to_bench_then_draw("fighting", 5), condition=hand_is_last()
)
