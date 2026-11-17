from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import colress_draw

card = SupporterCardDef(
    guid="5a2ed0ca-d5bf-55bb-aa66-5924901e2bc3",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Colress.Name",
    display_name="Colress",
    searchable_by=["Colress", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=135,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    effect=colress_draw()
)
