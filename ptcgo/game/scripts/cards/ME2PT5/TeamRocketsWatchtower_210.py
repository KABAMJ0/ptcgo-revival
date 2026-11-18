from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import abilities_off_for, pokemon_of

card = StadiumCardDef(
    guid="b5868bb7-94af-5ae4-a3f9-f09aa05fabb6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsWatchtower.Name",
    display_name="Team Rocket's Watchtower",
    searchable_by=["Team Rocket's Watchtower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=210,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=abilities_off_for(pokemon_of("colorless"))
)
