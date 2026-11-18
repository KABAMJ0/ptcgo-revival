from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, stadium_hp_bonus

card = StadiumCardDef(
    guid="f291686b-ab9d-55e2-b75b-ab1db734f26e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LivelyStadium.Name",
    display_name="Lively Stadium",
    searchable_by=["Lively Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=180,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    passive=stadium_hp_bonus(30, is_basic_pokemon)
)
