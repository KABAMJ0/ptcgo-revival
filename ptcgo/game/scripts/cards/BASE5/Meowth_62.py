from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def coin_hurl(ctx):
    """Choose 1 of their Pokemon, flip: heads does 20 with no Weakness or
    Resistance."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokemon")
    if target is None:
        return
    heads = await ctx.flip_coins(1, "Coin Hurl")
    if heads and heads[0]:
        await ctx.deal_damage(20, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="32f4aba0-439e-5626-b2ff-20780996413c",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth",
    searchable_by=["Meowth", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=52,
    abilities=[
        Attack(
            title="Coin Hurl",
            game_text="Choose 1 of your opponent's Pok\u00e9mon and flip a coin. If heads, this attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=coin_hurl,
        ),
    ],
)