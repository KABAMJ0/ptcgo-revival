from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_early_passive

card = StadiumCardDef(
    guid="fa8d1716-d7af-566e-87de-0d3735575c1f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofVitality.Name",
    display_name="Forest of Vitality",
    searchable_by=["Forest of Vitality", "Stadium"],
    subtypes=["Stadium"],
    collector_number=188,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=evolve_early_passive("grass")
)
