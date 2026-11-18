from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import excluding, is_evolution_pokemon, stadium_hp_bonus

card = StadiumCardDef(
    guid="f349fdc6-52b6-50d8-a701-0234e66b83f0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnowpointTemple.Name",
    display_name="Snowpoint Temple",
    searchable_by=["Snowpoint Temple", "Stadium"],
    subtypes=["Stadium"],
    collector_number=134,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(20, excluding(is_evolution_pokemon))
)
