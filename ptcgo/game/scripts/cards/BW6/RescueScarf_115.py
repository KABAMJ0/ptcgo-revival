from ptcgo.game.card_effects.passives_common import rescue_to_hand_on_attack_ko
from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="194759b5-60eb-5d11-96f9-7554d94329a1",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueScarf.Name",
    display_name="Rescue Scarf",
    searchable_by=["Rescue Scarf", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=115,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    passive=rescue_to_hand_on_attack_ko()
)
