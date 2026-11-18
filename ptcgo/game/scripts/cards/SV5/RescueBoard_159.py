from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import low_hp_retreat

card = PokemonToolCardDef(
    guid="eae6b14f-10f1-514c-8d68-c52845b1dc83",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueBoard.Name",
    display_name="Rescue Board",
    searchable_by=["Rescue Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=159,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    passive=low_hp_retreat(1, 30)
)
