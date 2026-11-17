from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import retaliate_on_attack

card = PokemonToolCardDef(
    guid="7c2465fb-3fe7-5bb8-9f47-13dac29ad29b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockGuard.Name",
    display_name="Rock Guard",
    searchable_by=["Rock Guard", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=108,
    set_code="BW9",
    rarity=Rarities.Rare,
    passive=retaliate_on_attack(6)
)
