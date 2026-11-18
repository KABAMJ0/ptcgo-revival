from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, identity_swap_from_discard, is_basic_pokemon, pokemon_of

card = SupporterCardDef(
    guid="6663cb21-4d5e-5fd4-b1c6-d4ca4913a512",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nanu.Name",
    display_name="Nanu",
    searchable_by=["Nanu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=identity_swap_from_discard(all_of(is_basic_pokemon, pokemon_of("darkness")))
)
