from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import retaliate_poison

card = PokemonToolCardDef(
    guid="b9cad71f-88b2-5d68-8769-ccc08ea903cf",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoisonBarb.Name",
    display_name="Poison Barb",
    searchable_by=["Poison Barb", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=124,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    passive=retaliate_poison()
)
