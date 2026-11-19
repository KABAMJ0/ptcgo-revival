from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.content.definitions import Triggers
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.session.effects import full_stack


async def _giant_fan(ctx):
    """On evolving: flip, and on heads the opponent shuffles 1 of their
    Pokemon and everything attached to it into their deck."""
    results = await ctx.flip_coins(1, "Giant Fan")
    if not (results and results[0]):
        return
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(
        pool, "Choose a Pok\u00e9mon to shuffle into your opponent's deck")
    if target is None:
        return
    await ctx.shuffle_into_deck(full_stack(target), target.owning_player_id)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab83561a-12cc-5dbf-aa6b-cd1c7da4f2b7",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=72,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Giant Fan",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may flip a coin. If heads, choose 1 of your opponent's Pok\u00e9mon. Your opponent shuffles that Pok\u00e9mon and all cards attached to it into his or her deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=_giant_fan,
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)