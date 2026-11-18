from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="0a1efd2c-c193-562f-9e36-2054c1b62a6a",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonRescue.Name",
    display_name="Pokémon Rescue",
    searchable_by=["Pok\u00e9mon Rescue", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=recover_from_discard(is_pokemon_card, count=1, to="hand", reveal=True)
)
