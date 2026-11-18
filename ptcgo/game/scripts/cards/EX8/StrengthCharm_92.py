from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import strength_charm_tool

card = PokemonToolCardDef(
    guid="619ee238-ff8b-5be5-870c-4f5d9312ff6a",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=strength_charm_tool(10, False, True, False),
)
