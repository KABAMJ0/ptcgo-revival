from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_boost_chosen

card = PokemonToolCardDef(
    guid="a989eae3-3ea3-5064-8f47-1d210c31dd17",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=150,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=turn_boost_chosen(10)
)
