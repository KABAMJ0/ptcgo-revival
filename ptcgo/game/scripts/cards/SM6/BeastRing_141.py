from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card, opponent_prizes_in, pokemon_of_subtype

card = ItemCardDef(
    guid="b74c928f-bf67-5d3d-9059-e00ffe40b7e3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name",
    display_name="Beast Ring",
    searchable_by=["Beast Ring", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    effect=search_attach_energy(is_basic_energy_card, count=2, target_pred=pokemon_of_subtype("Ultra Beast"), distribute=False), condition=opponent_prizes_in(3, 4)
)
