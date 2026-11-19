from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import lum_berry_between_turns

card = PokemonToolCardDef(
    guid="7180977e-b9d4-596b-ac0f-020469495a4e",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LumBerry.Name",
    display_name="Lum Berry",
    searchable_by=["Lum Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    granted_abilities=lum_berry_between_turns('Lum Berry'),
)
