from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_basic_pokemon, is_evolution_pokemon, shuffle_discard_combo_into_deck

card = ItemCardDef(
    guid="ed148e61-382d-587f-aeca-e7ff9a5bdda0",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightlyGarbageRun.Name",
    display_name="Nightly Garbage Run",
    searchable_by=["Nightly Garbage Run", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=77,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=shuffle_discard_combo_into_deck(3, any_of(is_basic_pokemon, is_evolution_pokemon, is_basic_energy_card))
)
