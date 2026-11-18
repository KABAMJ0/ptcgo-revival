from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import patrol_cap_tool

card = PokemonToolCardDef(
    guid="b763bd6b-c55e-53fa-826d-9e1fd920470c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PatrolCap.Name",
    display_name="Patrol Cap",
    searchable_by=["Patrol Cap", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=191,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    passive=patrol_cap_tool(),
)
