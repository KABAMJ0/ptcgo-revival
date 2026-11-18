from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_energy_opponent, with_discard_cost

card = SupporterCardDef(
    guid="16bc444e-26f7-5fbc-b21d-7655d5b2aba7",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    effect=with_discard_cost(2, discard_energy_opponent())
)
