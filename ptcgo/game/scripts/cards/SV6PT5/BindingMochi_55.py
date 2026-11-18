from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import SpecialConditions, holder_boost_when_conditioned

card = PokemonToolCardDef(
    guid="7da8b72f-6d18-56c6-b9e2-442a18b55511",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BindingMochi.Name",
    display_name="Binding Mochi",
    searchable_by=["Binding Mochi", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=55,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    passive=holder_boost_when_conditioned(40, SpecialConditions.POISONED)
)
