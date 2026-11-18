from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import any_of, is_basic_energy_card, is_pokemon_card

card = ItemCardDef(
    guid="d0a78f84-1b5e-5b93-a6ba-9f6a70bf9548",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightStretcher.Name",
    display_name="Night Stretcher",
    searchable_by=["Night Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=251,
    set_code="SV8",
    rarity=Rarities.Rare,
    effect=recover_from_discard(any_of(is_pokemon_card, is_basic_energy_card), count=1, to="hand")
)
