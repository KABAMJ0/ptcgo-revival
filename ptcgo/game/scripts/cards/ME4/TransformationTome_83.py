from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import identity_swap_from_discard, is_basic_pokemon

card = ItemCardDef(
    guid="f18b04f2-0260-565c-92d0-09eda43f788a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TransformationTome.Name",
    display_name="Transformation Tome",
    searchable_by=["Transformation Tome", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=identity_swap_from_discard(is_basic_pokemon),
)
