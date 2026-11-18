from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_for_shared_name

card = ItemCardDef(
    guid="cd37f2ff-8a76-5d83-bb71-24844fa471aa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArcadeGame.Name",
    display_name="Arcade Game",
    searchable_by=["Arcade Game", "Goldenrod Game Corner"],
    subtypes=["Goldenrod Game Corner"],
    collector_number=83,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=search_for_shared_name(3, 2)
)
