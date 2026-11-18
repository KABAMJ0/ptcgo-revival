from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import retreat_energy_to_hand

card = PokemonToolCardDef(
    guid="12426934-c087-57bc-afef-a4042c424aed",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DashingPouch.Name",
    display_name="Dashing Pouch",
    searchable_by=["Dashing Pouch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=retreat_energy_to_hand()
)
