from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import tool_discard_random_on_ko

card = PokemonToolCardDef(
    guid="84ae80d7-8887-52ac-8a99-671671cfc0fd",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursedDuster.Name",
    display_name="Cursed Duster",
    searchable_by=["Cursed Duster", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=161,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=tool_discard_random_on_ko(),
)
