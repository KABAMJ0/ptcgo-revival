from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, any_of, basic_energy_of, is_basic_pokemon, pokemon_of

card = ItemCardDef(
    guid="cb53e824-2d62-56f1-80ca-49ab7ff627a2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingGong.Name",
    display_name="Fighting Gong",
    searchable_by=["Fighting Gong", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(any_of(basic_energy_of("fighting"), all_of(is_basic_pokemon, pokemon_of("fighting"))), count=1)
)
