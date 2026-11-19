from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching, is_pokemon_ex

card = SupporterCardDef(
    guid="b5cb4fd0-47bb-5f4a-aa12-ab674497aecd",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=10027,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=evolve_from_deck_matching(exclude=is_pokemon_ex)
)
