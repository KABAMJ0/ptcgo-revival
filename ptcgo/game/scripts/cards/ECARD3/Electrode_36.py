from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


def _is_lightning_energy(card):
    return energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _plasma(ctx):
    await ctx.deal_damage()
    cards = [card for card in ctx.discard_pile() if _is_lightning_energy(card)]
    if not cards:
        return
    results = await ctx.flip_coins(1, "Plasma")
    if not (results and results[0]):
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=0,
        prompt="Choose a Lightning Energy card to attach to Electrode")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


async def _selfdestruct(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench() + ctx.opponent_bench():
        await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)
    await ctx.deal_damage(100, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="4538f30b-70ad-56d4-87eb-6eb4ccf8bbc9",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy card in your discard pile, flip a coin. If heads, attach 1 of them to Electrode.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=_plasma,
        ),
        Attack(
            title="Selfdestruct",
            game_text="This attack does 20 damage to each Pok\u00e9mon on each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Electrode does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=_selfdestruct,
        ),
    ],
)