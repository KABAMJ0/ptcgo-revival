from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f14bf81b-b33b-5bbe-a0a6-a04e8032438c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GlalieSpiritLink.Name",
    display_name="Glalie Spirit Link",
    searchable_by=["Glalie Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=139,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
