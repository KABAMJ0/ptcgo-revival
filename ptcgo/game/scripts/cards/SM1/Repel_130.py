from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_bench_to_active

card = ItemCardDef(
    guid="0ed8bc93-c59a-5542-93ce-a4649d7ccc9f",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Repel.Name",
    display_name="Repel",
    searchable_by=["Repel", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=opponent_bench_to_active(opponent_chooses=True)
)
