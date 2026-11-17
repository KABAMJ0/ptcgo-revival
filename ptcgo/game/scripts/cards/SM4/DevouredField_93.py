from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, stadium_damage_boost

card = StadiumCardDef(
    guid="e0b9123a-cf4c-5030-a17e-c52760d66796",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DevouredField.Name",
    display_name="Devoured Field",
    searchable_by=["Devoured Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=stadium_damage_boost(10, any_of(pokemon_of("darkness"), pokemon_of("dragon")), target=None)
)
