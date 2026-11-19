from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_all_attacks


async def power_rush(ctx):
    """120 damage. Flip a coin. If tails, this Pokémon can't attack during your next turn."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, "Power Rush"))[0]
    if not heads:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="1b64a1b2-0840-5c6f-8d87-1e6d49018e85",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=10016,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Oblivion Wing",
            game_text="Attach a Darkness Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Blade",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=power_rush,
        ),
    ],
)