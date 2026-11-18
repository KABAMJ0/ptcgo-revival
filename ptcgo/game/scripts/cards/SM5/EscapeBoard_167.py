from ptcgo.game.card_effects.passives_common import retreat_discount_despite_conditions
from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="da3fdfc3-309e-510a-8661-55db132b1fed",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=167,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    passive=retreat_discount_despite_conditions(1)
)
