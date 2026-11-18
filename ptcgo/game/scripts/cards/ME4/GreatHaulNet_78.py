from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, choose_any, pokemon_of

card = ItemCardDef(
    guid="bbbbda91-40aa-5f8f-9ee0-f3eb1bcb6e14",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreatHaulNet.Name",
    display_name="Great Haul Net",
    searchable_by=["Great Haul Net", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=choose_any([("Shuffle up to 3 Water Pokémon from your discard pile into your deck", recover_from_discard(pokemon_of("water"), count=3, to="deck_shuffle")), ("Shuffle up to 3 Basic Water Energy cards from your discard pile into y", recover_from_discard(basic_energy_of("water"), count=3, to="deck_shuffle"))])
)
