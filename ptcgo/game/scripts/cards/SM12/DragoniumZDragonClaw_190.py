from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import PokemonTypes
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.trainers import gx_attack_when_holder_has

_attack = Attack(
    title="Destructive Drake-GX",
    game_text="Discard all basic Energy from this Pok\u00e9mon. This attack does 80 damage for each card you discarded in this way. (You can't use more than 1 GX attack in a game.)",
    cost={PokemonTypes.COLORLESS: 3},
    damage=80,
    damage_operator="x",
    effect=self_energy_discard_attack(all_energy=True, then_damage=240),
)


card = PokemonToolCardDef(
    guid="ea7c61e1-4083-504f-b87a-1f3f72395048",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragoniumZDragonClaw.Name",
    display_name="Dragonium Z: Dragon Claw",
    searchable_by=["Dragonium Z: Dragon Claw", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=190,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=gx_attack_when_holder_has("Dragon Claw", _attack)
)
