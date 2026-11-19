from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import stadium_attack_tax, tera_attacker

card = StadiumCardDef(
    guid="54ec5ad4-248c-5e94-a4dc-82fc3847da14",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NighttimeMine.Name",
    display_name="Nighttime Mine",
    searchable_by=["Nighttime Mine", "Stadium"],
    subtypes=["Stadium"],
    collector_number=197,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=stadium_attack_tax(1, tera_attacker())
)
