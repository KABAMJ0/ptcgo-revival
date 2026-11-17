from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import low_hp_retreat

card = PokemonToolCardDef(
    guid="fbb7a30a-c34e-5809-96d9-f40acfea9ad4",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueBoard.Name",
    display_name="Rescue Board",
    searchable_by=["Rescue Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=126,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    passive=low_hp_retreat(1, 30)
)
