from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import extra_poison_counters, poison_not_of_type
from ptcgo.game.attributes import PokemonTypes

card = StadiumCardDef(
    guid="601ba66f-41b2-5a8d-8aee-8c5b55714810",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PerilousJungle.Name",
    display_name="Perilous Jungle",
    searchable_by=["Perilous Jungle", "Stadium"],
    subtypes=["Stadium"],
    collector_number=156,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=extra_poison_counters(2, pred=poison_not_of_type(PokemonTypes.DARKNESS.value))
)
