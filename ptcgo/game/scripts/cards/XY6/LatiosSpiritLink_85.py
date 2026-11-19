from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="75dab4eb-d11f-50a6-b054-0086c77f4437",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LatiosSpiritLink.Name",
    display_name="Latios Spirit Link",
    searchable_by=["Latios Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
