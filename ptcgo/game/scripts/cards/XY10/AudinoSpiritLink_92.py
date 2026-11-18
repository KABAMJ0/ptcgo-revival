from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="26df2f58-323a-5027-973f-e8969c4c3fdd",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AudinoSpiritLink.Name",
    display_name="Audino Spirit Link",
    searchable_by=["Audino Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
