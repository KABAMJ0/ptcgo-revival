from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_takes_less

card = PokemonToolCardDef(
    guid="e84f90d5-a938-5154-88f4-da81bc050c73",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockChestplate.Name",
    display_name="Rock Chestplate",
    searchable_by=["Rock Chestplate", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=192,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(30, protect_type="fighting")
)
