from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_search_deck_on_ko

card = PokemonToolCardDef(
    guid="9db92760-2c3f-5a5e-aef3-6697ab656e4c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmuletofHope.Name",
    display_name="Amulet of Hope",
    searchable_by=["Amulet of Hope", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=162,
    set_code="SV8",
    rarity=Rarities.Rare,
    on_carrier_knocked_out=tool_search_deck_on_ko(3),
)
