from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import attacker_has_special_energy, takes_less_from

card = PokemonToolCardDef(
    guid="f54a3999-16b8-5b65-abd8-76ea5df7846f",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AssaultVest.Name",
    display_name="Assault Vest",
    searchable_by=["Assault Vest", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=133,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=takes_less_from(40, None, attacker_has_special_energy())
)
