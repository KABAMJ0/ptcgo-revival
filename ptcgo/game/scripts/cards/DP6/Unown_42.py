from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.attacks_common import on_bench_play


async def _exclamation(ctx):
    """! : heads marks one of theirs, tails one of yours."""
    heads = await ctx.flip_coins(1, "!")
    pool = ctx.opponent_pokemon_in_play() if heads and all(heads) \
        else ctx.my_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokemon")
    if target is not None:
        await ctx.place_damage_counters(2, [target])

card = PokemonCardDef(
    guid="baf5f95f-95b3-5370-9604-cd747945ae17",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown [!]",
    searchable_by=["Unown [!]", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="!",
            game_text="Once during your turn, when you put Unown ! from your hand onto your Bench, you may flip a coin. If heads, put 2 damage counters on 1 of your opponent's Pok\u00e9mon. If tails, put 2 damage counters on 1 of your Pok\u00e9mon.",
                        trigger=Triggers.ON_PLAY,
            effect=on_bench_play(_exclamation),
        ),
        Attack(
            title="Hidden Power",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage. If tails, Unown ! does 10 damage to itself, and this attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)