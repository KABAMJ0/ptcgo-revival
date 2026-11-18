from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, hop, is_pokemon_card, owned_by, stadium_damage_boost

card = StadiumCardDef(
    guid="d3cca382-b136-5cb8-9d32-7744b74f21b9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Postwick.Name",
    display_name="Postwick",
    searchable_by=["Postwick", "Stadium"],
    subtypes=["Stadium"],
    collector_number=154,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    passive=stadium_damage_boost(30, all_of(is_pokemon_card, owned_by("hop")), target=None)
)
