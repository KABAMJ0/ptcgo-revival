from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="681302e4-2283-5bc9-bc88-945720719652",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AlakazamSpiritLink.Name",
    display_name="Alakazam Spirit Link",
    searchable_by=["Alakazam Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=90,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
