from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import stadium_no_resistance

card = StadiumCardDef(
    guid="1779582d-7441-57d7-bb84-662f9d817aba",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RuinsofAlph.Name",
    display_name="Ruins of Alph",
    searchable_by=["Ruins of Alph", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    passive=stadium_no_resistance()
)
