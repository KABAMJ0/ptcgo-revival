from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

async def _seafaring(ctx):
    """Flip 3; one Water Energy from the discard per head, attached to the
    Bench in any way you like."""
    results = await ctx.flip_coins(3, "Seafaring")
    heads = sum(1 for r in results if r)
    if heads <= 0:
        return
    predicate = basic_energy_of("water")
    cards = [c for c in ctx.discard_pile() if predicate(c)][:heads]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    for card in cards:
        holder = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Choose a Benched Pok\u00e9mon to attach the Energy to")
        if holder is None:
            break
        await ctx.attach_energy(card, holder)


card = PokemonCardDef(
    guid="ca174fe5-c0e9-5e72-aad1-bcd26f9f588a",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=_seafaring,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.WATER), per=20, base=10),
        ),
    ],
)