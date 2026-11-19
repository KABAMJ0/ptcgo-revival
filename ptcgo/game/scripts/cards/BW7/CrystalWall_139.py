from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_hp_bonus, card_named_contains

card = PokemonToolCardDef(
    guid="a0d9688a-ccfc-5803-ac3c-59fb5d05933f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalWall.Name",
    display_name="Crystal Wall",
    searchable_by=["Crystal Wall", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=139,
    set_code="BW7",
    rarity=Rarities.Rare,
    passive=gated_hp_bonus(120, card_named_contains("Black Kyurem"))
)
