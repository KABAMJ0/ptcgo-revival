from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_draw_until_on_ko

card = PokemonToolCardDef(
    guid="14a7695d-ff54-5e94-bbfa-f1dbfed733a1",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyEgg.Name",
    display_name="Lucky Egg",
    searchable_by=["Lucky Egg", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=88,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=tool_draw_until_on_ko(7),
)
