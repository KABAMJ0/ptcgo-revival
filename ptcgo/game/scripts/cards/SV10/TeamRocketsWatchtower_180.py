from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, pokemon_of

card = StadiumCardDef(
    guid="ec5cbd72-6e4a-57c2-94bf-df586f1ee13a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsWatchtower.Name",
    display_name="Team Rocket's Watchtower",
    searchable_by=["Team Rocket's Watchtower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=180,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(pokemon_of("colorless"))
)
