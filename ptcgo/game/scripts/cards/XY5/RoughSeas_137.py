from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, heal_where, pokemon_of, stadium_ability

card = StadiumCardDef(
    guid="c6fc8d01-d342-5e2a-891a-4fa09765b4c5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoughSeas.Name",
    display_name="Rough Seas",
    searchable_by=["Rough Seas", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Rough Seas', heal_where(30, "each_own", any_of(pokemon_of("water"), pokemon_of("lightning"))))
)
