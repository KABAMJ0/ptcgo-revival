from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="df46868a-bfab-5571-afec-ddea0d59691e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VenusaurSpiritLink.Name",
    display_name="Venusaur Spirit Link",
    searchable_by=["Venusaur Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=89,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
