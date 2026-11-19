from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_fire(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def _eruption(ctx):
    discarded = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, pid)
        if top:
            await ctx.discard_cards(top)
            discarded.extend(top)
    fire = sum(1 for card in discarded if _is_fire(card))
    await ctx.deal_damage(20 + 20 * fire)


async def _fire_stream(ctx):
    await ctx.deal_damage()
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=_is_fire, minimum=1,
        prompt="Choose a Fire Energy to discard from Magcargo")
    if not discarded:
        return
    for pokemon in ctx.opponent_bench():
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="f894c36e-e627-5e04-b9f9-6f59b91e61a2",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Eruption",
            game_text="Each player discard the top card of his or her deck. This attack does 20 damage plus 20 more damage for each Fire Energy card discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=_eruption,
        ),
        Attack(
            title="Fire Stream",
            game_text="Discard a Fire Energy card attached to Magcargo in order to use this attack. If your opponent has any Benched Pok\u00e9mon, this attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_fire_stream,
        ),
    ],
)
