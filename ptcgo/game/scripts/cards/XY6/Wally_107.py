from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching, is_pokemon_ex

card = SupporterCardDef(
    guid="5d792bae-2a1a-5062-ab73-98ed56ad628b",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=107,
    set_code="XY6",
    rarity=Rarities.RareUltra,
    effect=evolve_from_deck_matching(exclude=is_pokemon_ex)
)
