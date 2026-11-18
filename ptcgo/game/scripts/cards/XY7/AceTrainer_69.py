from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import behind_on_prizes, each_player_shuffle_draw_pair

card = SupporterCardDef(
    guid="a1cdecf5-5c0e-5f3c-bf0f-16e31db744d8",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AceTrainer.Name",
    display_name="Ace Trainer",
    searchable_by=["Ace Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=each_player_shuffle_draw_pair(6, 3), condition=behind_on_prizes()
)
