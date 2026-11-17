from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_damage_boost, named_rule_box

card = PokemonToolCardDef(
    guid="72d126ec-bc95-5c63-a4ee-2094d119d97a",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalEdge.Name",
    display_name="Crystal Edge",
    searchable_by=["Crystal Edge", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=138,
    set_code="BW7",
    rarity=Rarities.Rare,
    passive=gated_damage_boost(50, named_rule_box("white kyurem", "ex"))
)
