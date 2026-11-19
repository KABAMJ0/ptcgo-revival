from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import takes_less_passive, team_of_types
from ptcgo.game.attributes import Rarities, PokemonTypes

card = StadiumCardDef(
    guid="9b047b0c-08d7-59a2-9c03-dcf509f6f918",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherParadiseConservationArea.Name",
    display_name="Aether Paradise Conservation Area",
    searchable_by=["Aether Paradise Conservation Area", "Stadium"],
    subtypes=["Stadium"],
    collector_number=116,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(30, protects=team_of_types(PokemonTypes.GRASS.value, PokemonTypes.LIGHTNING.value, protects="each"))
)
