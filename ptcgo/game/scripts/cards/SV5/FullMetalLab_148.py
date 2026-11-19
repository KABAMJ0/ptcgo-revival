from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import takes_less_passive, team_of_types
from ptcgo.game.attributes import Rarities, PokemonTypes

card = StadiumCardDef(
    guid="40604de2-33bc-557c-bcbc-b23665cbb5e8",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullMetalLab.Name",
    display_name="Full Metal Lab",
    searchable_by=["Full Metal Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=148,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(30, protects=team_of_types(PokemonTypes.METAL.value, protects="each"))
)
