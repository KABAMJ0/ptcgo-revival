from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import heal_item
from ptcgo.game.card_effects.trainers import stadium_ability

card = StadiumCardDef(
    guid="2e6782c8-309d-59f9-b567-fae0359eac7a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Pokémon Center', heal_item(amount=20, scope="choice"))
)
