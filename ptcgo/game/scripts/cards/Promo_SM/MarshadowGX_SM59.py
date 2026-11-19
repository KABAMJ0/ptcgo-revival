from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def peerless_hundred_blows(ctx):
    """50 damage for each basic Energy card attached to this Pokemon."""
    from ptcgo.game.session.passives import is_basic_energy
    basic = [e for e in ctx.attached_energies(ctx.attacker) if is_basic_energy(e)]
    await ctx.deal_damage(50 * len(basic))


card = PokemonCardDef(
    guid="642dfe81-6a0b-52e2-a9b4-eb392c885693",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowGX.Name",
    display_name="Marshadow-GX",
    searchable_by=["Marshadow-GX", "Basic", "GX", "MarshadowGX"],
    subtypes=["Basic", "GX"],
    collector_number=59,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=802,
    abilities=[
        Ability(
            title="Shadow Hunt",
            game_text="This Pok\u00e9mon can use the attacks of Basic Pok\u00e9mon in your discard pile. (You still need the necessary Energy to use each attack.)",
            effect=unimplemented,
        ),
        Attack(
            title="Beatdown",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Peerless Hundred Blows-GX",
            game_text="This attack does 50 damage times the number of basic Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            effect=peerless_hundred_blows,
        ),
    ],
)