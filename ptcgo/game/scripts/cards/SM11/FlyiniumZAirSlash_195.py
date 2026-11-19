from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.trainers import gx_attack_when_holder_has

_attack = Attack(
    title="Speeding Skystrike-GX",
    game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 4},
    damage=180,
    effect=protect_next_turn(prevent=True, effects_too=True),
)


card = PokemonToolCardDef(
    guid="72c96a35-d391-5e6f-9a4f-0cf9670a8c41",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlyiniumZAirSlash.Name",
    display_name="Flyinium Z: Air Slash",
    searchable_by=["Flyinium Z: Air Slash", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=195,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=gx_attack_when_holder_has("Air Slash", _attack)
)
