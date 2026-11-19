from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def _exeggutor_scaled_snipe(ctx):
    attacker = ctx.attacker or ctx.source
    amount = 20 * len(ctx.attached_energies(attacker))
    pool = [p for p in ctx.opponent_bench() if p is not None]
    if ctx.opponent_active() is not None:
        pool.append(ctx.opponent_active())
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokémon")
    if target is not None:
        await ctx.deal_damage(amount, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="437c3481-74ed-59bb-a876-3fb37a0ca9ce",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorGX.Name",
    display_name="Alolan Exeggutor-GX",
    searchable_by=["Alolan Exeggutor-GX", "Stage 1", "GX", "AlolanExeggutorGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=107,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Head",
            game_text="This attack does 20 damage times the amount of Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=_exeggutor_scaled_snipe,
        ),
        Attack(
            title="Dragon Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Tower-Go-Round-GX",
            game_text="Move any number of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)