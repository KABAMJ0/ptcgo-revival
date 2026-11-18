from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_flip_draw

card = SupporterCardDef(
    guid="02c0375e-624c-5844-a267-3989077a1a8e",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lucian.Name",
    display_name="Lucian",
    searchable_by=["Lucian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SV6",
    rarity=Rarities.Rare,
    effect=each_player_shuffle_flip_draw(6, 3)
)
