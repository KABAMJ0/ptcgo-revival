from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import each_player_shuffle_draw

card = SupporterCardDef(
    guid="a9e7bc0c-c8dd-5c88-9c4e-d2e4fc0b03c9",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=78,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw(4)
)
