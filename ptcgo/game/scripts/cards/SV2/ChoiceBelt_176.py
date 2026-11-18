from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_damage_boost_vs

card = PokemonToolCardDef(
    guid="eed90cea-1424-58f3-83ec-9f9629521249",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBelt.Name",
    display_name="Choice Belt",
    searchable_by=["Choice Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=176,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    passive=holder_damage_boost_vs(30, "v")
)
