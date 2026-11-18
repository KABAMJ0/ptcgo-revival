from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.trainers import gx_attack_when_holder_has

_attack = Attack(
    title="Breakneck Blitz-GX",
    game_text="This attack does 50 damage times the number of Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 1},
    damage=50,
    damage_operator="x",
    effect=damage_per(count_energy('self'), 50),
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
