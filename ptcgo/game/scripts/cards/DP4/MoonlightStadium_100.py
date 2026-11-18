from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, pokemon_of, stadium_no_retreat

card = StadiumCardDef(
    guid="d2e3ee59-6e9b-5d3a-9458-91b129af9275",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoonlightStadium.Name",
    display_name="Moonlight Stadium",
    searchable_by=["Moonlight Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    passive=stadium_no_retreat(any_of(pokemon_of("psychic"), pokemon_of("darkness")))
)
