from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import retaliate_on_attack

card = PokemonToolCardDef(
    guid="a91c2c3a-e8ff-5fcb-bfd0-da0b4eb7151f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockyHelmet.Name",
    display_name="Rocky Helmet",
    searchable_by=["Rocky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=153,
    set_code="BW7",
    rarity=Rarities.RareSecret,
    passive=retaliate_on_attack(2)
)
