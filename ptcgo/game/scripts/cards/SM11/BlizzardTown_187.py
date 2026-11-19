from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import no_attack_at_hp

card = StadiumCardDef(
    guid="ffa144f0-2019-5f28-aae1-162235036ea5",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlizzardTown.Name",
    display_name="Blizzard Town",
    searchable_by=["Blizzard Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=187,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=no_attack_at_hp(40)
)
