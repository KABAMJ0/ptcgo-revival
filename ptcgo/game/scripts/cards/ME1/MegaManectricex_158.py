from ptcgo.game.card_effects.passives_common import protect_next_turn, attacker_is_basic
from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def riotous_blasting(ctx):
    """200; you may discard all Energy from this Pokemon to do 130 more."""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies and await ctx.ask_yes_no(
            "Discard all Energy from this Pokémon to do 130 more damage?"):
        await ctx.discard_energy_from(ctx.attacker, len(energies))
        await ctx.deal_damage(330)
        return
    await ctx.deal_damage(200)


card = PokemonCardDef(
    guid="cb589bf6-efbe-573f-a9db-bd41fc983148",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaManectricex.Name",
    display_name="Mega Manectric ex",
    searchable_by=["Mega Manectric ex", "Stage 1", "MEGA", "ex", "MegaManectricex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=158,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Flash Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Basic Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=120,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_basic()),
        ),
        Attack(
            title="Riotous Blasting",
            game_text="You may discard all Energy from this Pok\u00e9mon and have this attack do 130 more damage.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=200,
            damage_operator="+",
            effect=riotous_blasting,
        ),
    ],
)