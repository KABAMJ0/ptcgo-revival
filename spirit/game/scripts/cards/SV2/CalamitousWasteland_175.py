from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import all_of, excluding, is_basic_pokemon, pokemon_of, stadium_retreat_shift

card = StadiumCardDef(
    guid="27764a23-fd06-537f-a949-8b742e06b348",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CalamitousWasteland.Name",
    display_name="Calamitous Wasteland",
    searchable_by=["Calamitous Wasteland", "Stadium"],
    subtypes=["Stadium"],
    collector_number=175,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    passive=stadium_retreat_shift(1, all_of(is_basic_pokemon, excluding(pokemon_of("fighting"))))
)
