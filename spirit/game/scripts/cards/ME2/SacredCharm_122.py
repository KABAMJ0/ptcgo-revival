from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import attacker_has_ability, takes_less_from

card = PokemonToolCardDef(
    guid="ff2e0a0e-57fa-557c-87f8-021a590af7b1",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredCharm.Name",
    display_name="Sacred Charm",
    searchable_by=["Sacred Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="ME2",
    rarity=Rarities.Rare,
    passive=takes_less_from(30, None, attacker_has_ability())
)
