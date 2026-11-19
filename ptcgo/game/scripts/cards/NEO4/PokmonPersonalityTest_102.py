from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.card_effects.trainers import personality_test
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="58ef2c6c-602e-55ea-b203-84caaafbe1d8",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonPersonalityTest.Name",
    display_name="Pokémon Personality Test",
    searchable_by=["Pok\u00e9mon Personality Test"],
    subtypes=[],
    collector_number=102,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    effect=personality_test
)
