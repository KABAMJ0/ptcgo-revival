from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import evolve_early_passive

card = StadiumCardDef(
    guid="c129d64b-c635-5467-90c6-e78ea1cc2b6e",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestofVitality.Name",
    display_name="Forest of Vitality",
    searchable_by=["Forest of Vitality", "Stadium"],
    subtypes=["Stadium"],
    collector_number=109,
    set_code="ME3",
    rarity=Rarities.Rare,
    passive=evolve_early_passive("grass")
)
