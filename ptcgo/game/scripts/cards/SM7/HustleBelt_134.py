from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import low_hp_holder_boost

card = PokemonToolCardDef(
    guid="49e3b91b-b484-5d93-947b-c98ce10f2026",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name",
    display_name="Hustle Belt",
    searchable_by=["Hustle Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=134,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    passive=low_hp_holder_boost(60, 30)
)
