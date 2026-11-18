from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_trainer_to_deck

card = ItemCardDef(
    guid="ae3caa63-1d33-5ddd-b7df-0a59799625dd",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=72,
    set_code="BASE5",
    rarity=Rarities.Rare,
    effect=opponent_hand_trainer_to_deck(1)
)
