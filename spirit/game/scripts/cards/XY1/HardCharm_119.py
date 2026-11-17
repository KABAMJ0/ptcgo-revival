from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_takes_less

card = PokemonToolCardDef(
    guid="19d26a1b-854f-50cb-a065-43287acb1299",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HardCharm.Name",
    display_name="Hard Charm",
    searchable_by=["Hard Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=119,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=holder_takes_less(20)
)
