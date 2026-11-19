from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def blowing_wind(ctx):
    """Heads: one Benched Pokemon and everything attached goes on top of the deck."""
    results = await ctx.flip_coins(1, "Blowing Wind")
    bench = list(ctx.my_bench())
    if not (results and results[0]) or not bench:
        return
    pick = await ctx.choose_pokemon(bench, "Choose a Benched Pok\u00e9mon")
    if pick is None:
        return
    stack = [pick]
    pending = [pick]
    while pending:
        entity = pending.pop()
        for child in list(entity.children):
            stack.append(child)
            pending.append(child)
    for card in stack:
        await ctx.put_on_top_of_deck(card)
    await ctx.shuffle_deck()
card = PokemonCardDef(
    guid="6eb06cd6-e409-5ad4-9f16-c5473424ca14",
    key="POP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="POP6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=425,
    abilities=[
        Attack(
            title="Blowing Wind",
            game_text="Flip a coin. If heads, put 1 of your Benched Pok\u00e9mon and all cards attached to it on top of your deck. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=blowing_wind,
        ),
        Attack(
            title="Ominous Wind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)