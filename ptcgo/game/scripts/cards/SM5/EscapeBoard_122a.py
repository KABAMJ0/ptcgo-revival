from ptcgo.game.card_effects.passives_common import retreat_discount_despite_conditions
from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="4b14e000-3a65-5555-8cb4-3dd6cafde104",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=retreat_discount_despite_conditions(1)
)
