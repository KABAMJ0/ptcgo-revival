from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="42e94428-abd4-539d-ad6b-d0c8f89d9855",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MewtwoSpiritLink.Name",
    display_name="Mewtwo Spirit Link",
    searchable_by=["Mewtwo Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=144,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
