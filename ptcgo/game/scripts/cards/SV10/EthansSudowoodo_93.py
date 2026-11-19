from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import def_for
from ptcgo.game.attributes import AttrID


async def mini_metronome(ctx):
    """Flip a coin. If heads, choose 1 of your opponent's Active Pokemon's attacks and use it as this attack."""
    heads = await ctx.flip_coins(1, ctx.ability.title)
    if not heads[0]:
        return
    defender = ctx.opponent_active()
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    candidates = [
        (defender, ability) for ability in getattr(definition, "abilities", [])
        if isinstance(ability, Attack)
    ]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    if not await ctx.use_attack(chosen):
        return
    if getattr(chosen, "locks_next_turn", False):
        for entry in ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or []:
            if isinstance(entry, dict) and entry.get("abilityType") == "Attack":
                ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, entry["abilityID"])


card = PokemonCardDef(
    guid="abce8386-f187-5935-91ba-c1993548c5f5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSudowoodo.Name",
    display_name="Ethan's Sudowoodo",
    searchable_by=["Ethan's Sudowoodo", "Basic", "EthansSudowoodo"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Attack(
            title="Impound",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Try to Imitate",
            game_text="Flip a coin. If heads, choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=mini_metronome,
        ),
    ],
)