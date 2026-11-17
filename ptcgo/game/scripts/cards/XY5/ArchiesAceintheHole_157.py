from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_typed_pokemon_to_bench_then_draw, hand_is_last

card = SupporterCardDef(
    guid="e3b7848d-04cc-59df-a460-9f2d8f422c32",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArchiesAceintheHole.Name",
    display_name="Archie's Ace in the Hole",
    searchable_by=["Archie's Ace in the Hole", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    effect=discard_typed_pokemon_to_bench_then_draw("water", 5), condition=hand_is_last()
)
