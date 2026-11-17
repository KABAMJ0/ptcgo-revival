from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import rare_candy

card = ItemCardDef(
    guid="29584248-5400-52cf-a06d-6585ea159f1b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder"],
    subtypes=[],
    collector_number=76,
    set_code="BASE1",
    rarity=Rarities.Rare,
    effect=rare_candy()
)
