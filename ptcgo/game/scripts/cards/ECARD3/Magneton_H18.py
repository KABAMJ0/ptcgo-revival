from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_lightning(card) -> bool:
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _electric_blast(ctx):
    await ctx.deal_damage()
    lightning = [e for e in ctx.attached_energies(ctx.attacker) if _is_lightning(e)]
    if not lightning:
        return
    if not await ctx.ask_yes_no(
            "Discard all Lightning Energy attached to Magneton?"):
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 99, predicate=_is_lightning,
        prompt="Choose Lightning Energy to discard from Magneton")
    bench = ctx.opponent_bench()
    if discarded and bench:
        await ctx.place_damage_counters(len(discarded), bench)

card = PokemonCardDef(
    guid="d015a81a-2205-54c5-a271-ada3dcfefaca",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Ability(
            title="Attract Energy",
            game_text="When you play Magneton from your hand to evolve 1 of your Pok\u00e9mon, you may move any number of basic Energy cards attached to your other Pok\u00e9mon to Magneton.",
            effect=unimplemented,
        ),
        Attack(
            title="Electric Blast",
            game_text="You may discard all Lightning Energy cards attached to Magneton when you use this attack. If you do, put damage counters equal to the amount of Energy cards removed in this way on any number of your opponent's Benched Pok\u00e9mon in the way you like. (For example, if you discard 3 Lightning Energy cards, you can put 1 damage counter on 1 of your opponent's Benched Pok\u00e9mon and 2 on another.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_electric_blast,
        ),
    ],
)
