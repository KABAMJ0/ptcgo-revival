from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import low_hp_holder_boost

card = PokemonToolCardDef(
    guid="bac1091a-a266-56bc-9231-bd9b8cc614eb",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name",
    display_name="Hustle Belt",
    searchable_by=["Hustle Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=179,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    passive=low_hp_holder_boost(60, 30)
)
