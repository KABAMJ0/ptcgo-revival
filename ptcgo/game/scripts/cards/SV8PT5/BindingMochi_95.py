from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import SpecialConditions, holder_boost_when_conditioned

card = PokemonToolCardDef(
    guid="ce430a32-1045-5825-a30d-a76e7c68988b",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BindingMochi.Name",
    display_name="Binding Mochi",
    searchable_by=["Binding Mochi", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=95,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    passive=holder_boost_when_conditioned(40, SpecialConditions.POISONED)
)
