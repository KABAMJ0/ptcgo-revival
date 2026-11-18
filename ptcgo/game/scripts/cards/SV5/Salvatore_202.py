from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching

card = SupporterCardDef(
    guid="4b8b2b5e-a830-52f9-890e-735fd731264e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Salvatore.Name",
    display_name="Salvatore",
    searchable_by=["Salvatore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=202,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=evolve_from_deck_matching(lambda card: not getattr(card, "abilities", None))
)
