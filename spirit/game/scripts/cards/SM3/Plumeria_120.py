from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_energy_opponent, with_discard_cost

card = SupporterCardDef(
    guid="081907e9-09b4-59a9-be15-a5d82e91d927",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(2, discard_energy_opponent())
)
