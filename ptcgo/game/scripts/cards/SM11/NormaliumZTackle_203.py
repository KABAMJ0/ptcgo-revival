from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.trainers import gx_attack_when_holder_has

_attack = Attack(
    title="Barreling Blitz-GX",
    game_text="Flip a coin until you get tails. This attack does 40 more damage for each heads. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 4},
    damage=200,
    damage_operator="+",
    effect=flip_damage(per_heads=40, base=200, until_tails=True),
)


card = PokemonToolCardDef(
    guid="e0e79950-9af0-52af-b325-ef747d9ba488",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NormaliumZTackle.Name",
    display_name="Normalium Z: Tackle",
    searchable_by=["Normalium Z: Tackle", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=203,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    passive=gx_attack_when_holder_has("Tackle", _attack)
)
