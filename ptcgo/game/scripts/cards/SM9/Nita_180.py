from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, opponent_active_energy_to_deck_top, opponent_active_is

card = SupporterCardDef(
    guid="57d76f7d-3945-5fa2-9f05-70c2b717c650",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=opponent_active_energy_to_deck_top(1), condition=opponent_active_is(is_basic_pokemon)
)
