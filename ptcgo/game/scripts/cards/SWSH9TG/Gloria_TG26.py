from ptcgo.game.data_utils import SupporterCardDef, has_rule_box
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon


def _no_rule_box_basic(card) -> bool:
    return is_basic_pokemon(card) and not has_rule_box(card.archetype_id)


card = SupporterCardDef(
    guid="8d249eef-52d2-52bd-8f96-892f3f2bba08",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gloria.Name",
    display_name="Gloria",
    searchable_by=["Gloria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=26,
    set_code="SWSH9TG",
    rarity=Rarities.RareUltra,
    effect=search_to_bench(
        _no_rule_box_basic, count=3,
        prompt="Choose up to 3 Basic Pokémon without a Rule Box to put onto your Bench.",
    )
)
