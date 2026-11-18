from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_trainer_to_deck

card = ItemCardDef(
    guid="38c2c2ae-749d-5f3f-bb8b-85ab5e30693c",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSneakAttack.Name",
    display_name="Rocket's Sneak Attack",
    searchable_by=["Rocket's Sneak Attack"],
    subtypes=[],
    collector_number=16,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    effect=opponent_hand_trainer_to_deck(1)
)
