from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import (
    is_in_active_spot, prevent_damage_when,
)


async def anger_revenge(ctx):
    """60, then 40 to a chosen Benched Pokemon when Bastiodon was damaged by an
    attack during the opponent's last turn."""
    await ctx.deal_damage(60)
    if ctx.attacker is None or not ctx.damaged_by_attack_last_turn(ctx.attacker):
        return
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    pick = await ctx.choose_pokemon(bench, "Choose a Benched Pok\u00e9mon")
    if pick is None:
        return
    await ctx.deal_damage(40, target=pick, apply_modifiers=False)


def _protects_own_bench(calc, carrier) -> bool:
    return (calc.target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(calc.target))


card = PokemonCardDef(
    guid="97355b86-2b6b-53ab-b2f1-46626e02761c",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bastiodon.Name",
    display_name="Bastiodon",
    searchable_by=["Bastiodon", "Stage 2", "Bastiodon"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="POP6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shieldon.Name",
    family_id=411,
    abilities=[
        Ability(
            title="Protective Wall",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            passive=prevent_damage_when(_protects_own_bench),
        ),
        Attack(
            title="Anger Revenge",
            game_text="If Bastiodon was damaged by an attack during your opponent's last turn, this attack does 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=anger_revenge,
        ),
    ],
)