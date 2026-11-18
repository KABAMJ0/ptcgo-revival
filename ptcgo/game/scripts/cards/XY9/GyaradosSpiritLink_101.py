from ptcgo.game.card_effects.passives_common import spirit_link_passive
from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="961fe2e5-7fe1-5bc4-9079-a98901a6ed54",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GyaradosSpiritLink.Name",
    display_name="Gyarados Spirit Link",
    searchable_by=["Gyarados Spirit Link", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=101,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    passive=spirit_link_passive(),
)
