from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, any_of, card_named_contains, is_basic_pokemon, is_evolution_pokemon, trade_hand_for_deck

card = ItemCardDef(
    guid="113c011b-e436-551c-ae53-2dac3cff60c7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasMaids.Name",
    display_name="Erika's Maids",
    searchable_by=["Erika's Maids"],
    subtypes=[],
    collector_number=109,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=trade_hand_for_deck(2, all_of(any_of(is_basic_pokemon, is_evolution_pokemon), card_named_contains('erika')), 2)
)
