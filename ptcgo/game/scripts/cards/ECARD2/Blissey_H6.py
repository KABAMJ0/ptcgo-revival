from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.attacks_common import flip_damage

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.session.passives import effective_max_hp
from ptcgo.game.attributes import AttrID


def _happy_healing_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
               for p in (bench.children if bench else []))


async def _happy_healing(ctx):
    bench = ctx.my_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to heal")
    if target is None:
        return
    results = await ctx.flip_coins(1, "Happy Healing")
    if not (results and results[0]):
        return
    counters = len(ctx.attached_energies(ctx.attacker))
    if counters > 0:
        await ctx.heal(10 * counters, target)


card = PokemonCardDef(
    guid="c69163a2-6331-5ab5-9568-069c6d6b5de4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Ability(
            title="Happy Healing",
            game_text="Once during your turn (before your attack), choose 1 of your Benched Pok\u00e9mon and flip a coin. If heads, count the number of Energy attached to Blissey and then remove that many damage counters from the chosen Benched Pok\u00e9mon. This power can't be used if Blissey is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_happy_healing_available,
            effect=_happy_healing,
        ),
        Attack(
            title="Smash Bomber",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=flip_or_nothing(),
        ),
    ],
)