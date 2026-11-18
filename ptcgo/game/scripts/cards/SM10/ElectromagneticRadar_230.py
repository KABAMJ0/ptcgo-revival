from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import any_of, pokemon_type_subtype, with_discard_cost

card = ItemCardDef(
    guid="d91e92fc-a188-52af-910d-c2d639f7d86f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElectromagneticRadar.Name",
    display_name="Electromagnetic Radar",
    searchable_by=["Electromagnetic Radar", "Item"],
    subtypes=["Item"],
    collector_number=230,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    effect=with_discard_cost(2, search_to_hand(any_of(pokemon_type_subtype("lightning", "gx"), pokemon_type_subtype("lightning", "ex")), count=2))
)
