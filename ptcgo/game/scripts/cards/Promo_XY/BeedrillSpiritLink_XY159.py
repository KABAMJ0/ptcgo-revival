from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="2c1ddbf0-e0e9-5a3c-a071-52f5553dea7b",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeedrillSpiritLink.Name",
    display_name="Beedrill Spirit Link",
    searchable_by=["Beedrill Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=159,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    passive=spirit_link_passive(),
)
