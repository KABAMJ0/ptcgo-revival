from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import low_hp_retreat

card = PokemonToolCardDef(
    guid="cd0a19e0-c23d-5c91-8e6e-8c588c8fdb6b",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueBoard.Name",
    display_name="Rescue Board",
    searchable_by=["Rescue Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=225,
    set_code="SV6",
    rarity=Rarities.Rare,
    passive=low_hp_retreat(1, 30)
)
