from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import balloon_berry_passive

card = PokemonToolCardDef(
    guid="aa5139df-9e98-52e2-9333-93f2df26d571",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=82,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=balloon_berry_passive(),
)
