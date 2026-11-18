from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching, is_pokemon_ex

card = SupporterCardDef(
    guid="8d4936df-2de0-5d10-8fec-9cc3596d8db0",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=94,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=evolve_from_deck_matching(exclude=is_pokemon_ex)
)
