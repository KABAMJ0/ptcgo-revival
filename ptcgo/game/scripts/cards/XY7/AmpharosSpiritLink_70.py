from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="5d2a67b8-622d-59ef-96e3-98568fd23577",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AmpharosSpiritLink.Name",
    display_name="Ampharos Spirit Link",
    searchable_by=["Ampharos Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=70,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
