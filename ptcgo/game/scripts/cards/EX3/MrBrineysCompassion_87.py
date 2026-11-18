from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, excluding, is_pokemon_card, is_pokemon_ex, return_pokemon_to_hand

card = SupporterCardDef(
    guid="5b5fbb62-9deb-5d0f-b292-ea82dbc5d051",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrBrineysCompassion.Name",
    display_name="Mr. Briney's Compassion",
    searchable_by=["Mr. Briney's Compassion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(predicate=all_of(is_pokemon_card, excluding(is_pokemon_ex)))
)
