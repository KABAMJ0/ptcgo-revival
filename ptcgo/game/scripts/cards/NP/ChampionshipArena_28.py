from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = StadiumCardDef(
    guid="9ee1eb42-ac0d-5d23-b89d-4af5ae9b6022",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionshipArena.Name",
    display_name="Championship Arena",
    searchable_by=["Championship Arena", "Stadium"],
    subtypes=["Stadium"],
    collector_number=28,
    set_code="NP",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
