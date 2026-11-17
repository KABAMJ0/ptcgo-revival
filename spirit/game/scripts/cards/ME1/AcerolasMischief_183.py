from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_prizes_at_most, protect_chosen_next_turn

card = SupporterCardDef(
    guid="e60eb2c5-f2aa-5eaf-bcc1-d82908b62a2e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcerolasMischief.Name",
    display_name="Acerola's Mischief",
    searchable_by=["Acerola's Mischief", "Supporter"],
    subtypes=["Supporter"],
    collector_number=183,
    set_code="ME1",
    rarity=Rarities.Rare,
    effect=protect_chosen_next_turn(1), condition=opponent_prizes_at_most(2)
)
