from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.card_effects.trainers import balloon_berry_passive

card = PokemonToolCardDef(
    guid="ff9325fa-57c2-59c4-a1dd-04098990c761",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=60,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    passive=balloon_berry_passive(),
)
