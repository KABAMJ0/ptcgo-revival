from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import hand_card_to_top, hand_size_at_least, pokemon_of_subtype
from ptcgo.game.card_effects.support_common import search_to_hand


_SP_RADAR = composed(
    hand_card_to_top(),
    then=search_to_hand(pokemon_of_subtype("SP"), count=1, minimum=0,
                        reveal=True,
                        prompt="Choose a Pok\u00e9mon SP to put into your hand"))


card = ItemCardDef(
    guid="e51d11cc-9321-5711-bf6b-57a8752adea7",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsInventionG109SPRadar.Name",
    display_name="Team Galactic's Invention G-109 SP Radar",
    searchable_by=["Team Galactic's Invention G-109 SP Radar", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    effect=_SP_RADAR,
    condition=hand_size_at_least(2),
)
