from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_typed_pokemon_to_bench_then_draw, hand_is_last

card = SupporterCardDef(
    guid="5e2efbe1-2f95-58b8-b68e-9bdea3db53d2",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name",
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=discard_typed_pokemon_to_bench_then_draw("water", 5), condition=hand_is_last()
)
