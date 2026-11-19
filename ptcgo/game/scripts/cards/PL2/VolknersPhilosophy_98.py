from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import optional_discard_draw_until

card = SupporterCardDef(
    guid="71f30a26-383e-5d0e-9b30-17ccd6df1265",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VolknersPhilosophy.Name",
    display_name="Volkner's Philosophy",
    searchable_by=["Volkner's Philosophy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=optional_discard_draw_until(6)
)
