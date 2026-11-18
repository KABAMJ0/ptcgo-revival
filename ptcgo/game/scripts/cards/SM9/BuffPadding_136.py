from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hp_bonus_tool, retreat_cost_is

card = PokemonToolCardDef(
    guid="b7ced02f-ca3b-5aaa-a021-a9a26ba63f12",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuffPadding.Name",
    display_name="Buff Padding",
    searchable_by=["Buff Padding", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=136,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(50, retreat_cost_is(4))
)
