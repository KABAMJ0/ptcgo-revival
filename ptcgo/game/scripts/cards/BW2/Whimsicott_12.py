from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack


def _printed_attacks(pokemon):
    return [entry for entry in (pokemon.get_attribute(AttrID.PIE_ABILITIES) or [])
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack"
            and entry.get("abilityID")]


async def _encore(ctx):
    """Choose 1 of the Defending Pokemon's attacks; through the opponent's
    next turn that Pokemon can only use it. The engine has no allow-list, so
    every other printed attack is locked instead, which is the same rule."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    from ptcgo.game.content.definitions import ABILITIES_BY_ID
    entries = _printed_attacks(defender)
    choices = [ABILITIES_BY_ID.get(entry["abilityID"]) for entry in entries]
    choices = [choice for choice in choices if choice is not None]
    if len(choices) < 2:
        return
    chosen = choices[0] if len(choices) == 1 else \
        await ctx.choose_attack_to_copy(choices, "Choose an attack to keep")
    if chosen is None:
        return
    state = ctx.session.turn_state
    for choice in choices:
        if choice.ability_id != chosen.ability_id:
            state.attack_locks[(defender.entity_id, choice.ability_id)] = \
                state.turn_number + 1


card = PokemonCardDef(
    guid="6b482de6-0d68-5459-9cf5-edeb768cdb0b",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1", "Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Encore",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. During your opponent's next turn, that Pok\u00e9mon can only use that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_encore,
        ),
        Attack(
            title="U-turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)