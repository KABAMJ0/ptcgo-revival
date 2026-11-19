from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.passives_common import (
    apply_protection, attacker_is_basic,
)


async def quick_guard(ctx):
    """Prevent all damage from Basic attackers through the opponent's next
    turn; Quick Guard itself is locked for its user's next turn."""
    await apply_protection(ctx, prevent=True, attacker_pred=attacker_is_basic())
    attacker = ctx.attacker
    ability_id = getattr(ctx.ability, "ability_id", None)
    if attacker is not None and ability_id:
        ctx.session.turn_state.lock_attack(attacker.entity_id, ability_id)


card = PokemonCardDef(
    guid="1834d977-16a9-5458-aaa4-cbdafeb1cd89",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Quick Guard",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon during your opponent's next turn. This Pok\u00e9mon can't use Quick Guard during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=quick_guard,
        ),
        Attack(
            title="Brick Break",
            game_text="This attack's damage isn't affected by Resistance or any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)