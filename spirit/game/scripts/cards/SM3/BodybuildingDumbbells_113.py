from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_hp_bonus, is_stage_one

card = PokemonToolCardDef(
    guid="cf91b818-3007-5cb6-ae83-b961cf0135b2",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BodybuildingDumbbells.Name",
    display_name="Bodybuilding Dumbbells",
    searchable_by=["Bodybuilding Dumbbells", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=113,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    passive=gated_hp_bonus(40, is_stage_one)
)
