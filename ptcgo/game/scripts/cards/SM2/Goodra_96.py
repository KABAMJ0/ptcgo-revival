from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

async def _goodra_scaled_snipe(ctx):
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
    guid="a57cb90f-cee9-5967-ad18-3615c866465d",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2", "Goodra"],
    subtypes=["Stage 2"],
    collector_number=96,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Attack(
            title="Power Whip",
            game_text="This attack does 20 damage times the amount of Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_goodra_scaled_snipe,
        ),
        Attack(
            title="Beat Slider",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)