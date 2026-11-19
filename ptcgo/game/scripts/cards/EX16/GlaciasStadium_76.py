from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_no_weakness, all_of, pokemon_of, excluding, is_pokemon_EX

card = StadiumCardDef(
    guid="4b488e3f-e650-59ad-9c65-a215393f3d1d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlaciasStadium.Name",
    display_name="Glacia's Stadium",
    searchable_by=["Glacia's Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    passive=stadium_no_weakness(all_of(pokemon_of("water"), excluding(is_pokemon_EX)))
)
