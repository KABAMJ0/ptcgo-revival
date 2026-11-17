from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import pokemon_named, stadium_retreat_shift

card = StadiumCardDef(
    guid="612f6bbd-5db7-5e70-8138-5c193560b724",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParadiseResort.Name",
    display_name="Paradise Resort",
    searchable_by=["Paradise Resort", "Stadium"],
    subtypes=["Stadium"],
    collector_number=45,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    passive=stadium_retreat_shift(-1, pokemon_named("psyduck"))
)
