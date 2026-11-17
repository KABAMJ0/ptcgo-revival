from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import pokemon_of, stadium_prize_shift

card = StadiumCardDef(
    guid="45d042ed-8cbc-5cea-afec-e73914dba6cb",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LegendarySummit.Name",
    display_name="Legendary Summit",
    searchable_by=["Legendary Summit", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    passive=stadium_prize_shift(-1, pokemon_of("colorless"))
)
