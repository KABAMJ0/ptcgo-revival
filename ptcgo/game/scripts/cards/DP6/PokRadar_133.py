from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top
from ptcgo.game.card_effects.trainers import is_pokemon_card

card = ItemCardDef(
    guid="c8e5bfee-d222-5d51-84c1-ab0b05f1a45a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokRadar.Name",
    display_name="Poké Radar",
    searchable_by=["Pok\u00e9 Radar", "Item"],
    subtypes=["Item"],
    collector_number=133,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=look_at_top(5, take=5, predicate=is_pokemon_card, minimum=0)
)
