from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_draw

card = SupporterCardDef(
    guid="04c7d732-8c5b-524e-a91b-7ac646cc7f9e",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmceesChatter.Name",
    display_name="Emcee's Chatter",
    searchable_by=["Emcee's Chatter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=flip_draw(3, 2)
)
