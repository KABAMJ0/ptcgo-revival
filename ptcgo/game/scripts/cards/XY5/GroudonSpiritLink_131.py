from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="0184f277-0cee-5608-ac16-3e719b735552",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GroudonSpiritLink.Name",
    display_name="Groudon Spirit Link",
    searchable_by=["Groudon Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=131,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
