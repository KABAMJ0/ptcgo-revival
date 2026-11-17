from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_at_most, protect_chosen_next_turn

card = SupporterCardDef(
    guid="3275c8d1-1b80-5ee0-a9e8-0629c90ddf33",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcerolasMischief.Name",
    display_name="Acerola's Mischief",
    searchable_by=["Acerola's Mischief", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=protect_chosen_next_turn(1), condition=opponent_prizes_at_most(2)
)
