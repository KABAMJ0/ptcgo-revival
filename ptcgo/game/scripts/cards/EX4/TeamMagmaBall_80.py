from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import team_magma_ball

card = ItemCardDef(
    guid="918dc69a-2573-5528-a2c9-c892c386e373",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBall.Name",
    display_name="Team Magma Ball",
    searchable_by=["Team Magma Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    effect=team_magma_ball()
)
