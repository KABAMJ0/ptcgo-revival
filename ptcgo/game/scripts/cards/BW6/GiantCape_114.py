from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_hp_bonus

card = PokemonToolCardDef(
    guid="de2772ee-ed13-56d2-a2b3-b8dc1e726c47",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantCape.Name",
    display_name="Giant Cape",
    searchable_by=["Giant Cape", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=114,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=holder_hp_bonus(20)
)
