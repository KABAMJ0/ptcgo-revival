from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import pokemon_named, stadium_retreat_shift

card = StadiumCardDef(
    guid="482c957e-2f65-50de-9818-40fdfe298843",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ParadiseResort.Name",
    display_name="Paradise Resort",
    searchable_by=["Paradise Resort", "Stadium"],
    subtypes=["Stadium"],
    collector_number=150,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    passive=stadium_retreat_shift(-1, pokemon_named("psyduck"))
)
