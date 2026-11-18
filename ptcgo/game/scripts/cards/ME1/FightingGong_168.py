from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, basic_energy_of, is_basic_pokemon, pokemon_of

card = ItemCardDef(
    guid="057bf947-c778-513d-934e-5553a268367b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingGong.Name",
    display_name="Fighting Gong",
    searchable_by=["Fighting Gong", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=search_to_hand(any_of(basic_energy_of("fighting"), all_of(is_basic_pokemon, pokemon_of("fighting"))), count=1)
)
