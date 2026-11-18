from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import balloon_berry_passive

card = PokemonToolCardDef(
    guid="9127027c-8219-5bfa-b861-203464b0e059",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    passive=balloon_berry_passive(),
)
