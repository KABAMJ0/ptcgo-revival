from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_basic_pokemon, is_evolution_pokemon, pokemon_of_subtype, shuffle_discard_combo_into_deck

card = SupporterCardDef(
    guid="5d9ef73a-c3e2-58c5-ab14-6f9d146b056c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TownVolunteers.Name",
    display_name="Town Volunteers",
    searchable_by=["Town Volunteers", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    effect=shuffle_discard_combo_into_deck(5, any_of(pokemon_of_subtype('Baby'), is_basic_pokemon, is_evolution_pokemon, is_basic_energy_card))
)
