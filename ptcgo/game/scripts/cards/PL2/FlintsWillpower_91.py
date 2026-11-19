from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, pokemon_of_subtype
from ptcgo.game.card_effects.support_common import attach_from_hand


card = SupporterCardDef(
    guid="421f8f5c-33d0-54a9-8a4e-066234cb82c1",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlintsWillpower.Name",
    display_name="Flint's Willpower",
    searchable_by=["Flint's Willpower", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=attach_from_hand(
        is_basic_energy_card, count=1, target="choice",
        target_pred=pokemon_of_subtype("SP"),
        prompt="Choose a basic Energy card to attach to 1 of your Pok\u00e9mon SP"),
)
