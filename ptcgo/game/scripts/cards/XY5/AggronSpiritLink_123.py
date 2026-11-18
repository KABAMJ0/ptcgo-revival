from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f77d9ee0-9cce-5327-b761-1daf01b36b05",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AggronSpiritLink.Name",
    display_name="Aggron Spirit Link",
    searchable_by=["Aggron Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=123,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
