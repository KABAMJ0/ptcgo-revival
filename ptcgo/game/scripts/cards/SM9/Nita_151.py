from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, opponent_active_energy_to_deck_top, opponent_active_is

card = SupporterCardDef(
    guid="03b884f8-71a8-568c-af53-370d48ae2ebb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=opponent_active_energy_to_deck_top(1), condition=opponent_active_is(is_basic_pokemon)
)
