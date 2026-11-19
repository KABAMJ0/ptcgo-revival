from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def peerless_hundred_blows_gx(ctx):
    """50 damage for each basic Energy card attached to this Pokemon."""
    count = sum(1 for energy in ctx.attached_energies(ctx.attacker)
                if is_basic_energy_card(energy))
    if count:
        await ctx.deal_damage(50 * count)


card = PokemonCardDef(
    guid="a84f6d50-989b-547e-8a6c-fe7e7562c634",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarshadowGX.Name",
    display_name="Marshadow-GX",
    searchable_by=["Marshadow-GX", "Basic", "GX", "MarshadowGX"],
    subtypes=["Basic", "GX"],
    collector_number=137,
    set_code="SM3",
    rarity=Rarities.RareUltra,
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
            game_text="This attack does 50 damage times the amount of basic Energy attached to this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="x",
            effect=peerless_hundred_blows_gx,
        ),
    ],
)