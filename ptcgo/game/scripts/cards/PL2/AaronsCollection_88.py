from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, pokemon_of_subtype

card = SupporterCardDef(
    guid="b865889d-e25a-5dda-9f89-de2ec0520005",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AaronsCollection.Name",
    display_name="Aaron's Collection",
    searchable_by=["Aaron's Collection", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(any_of(pokemon_of_subtype("SP"), is_basic_energy_card), count=2, to="hand", reveal=True)
)
