from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import lost_mine_condition

async def lost_impact(ctx):
    """280. Put 2 Energy attached to your Pokemon in the Lost Zone."""
    await ctx.deal_damage()
    energies = []
    for pokemon in ctx.my_pokemon_in_play():
        energies.extend(ctx.attached_energies(pokemon))
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2,
        prompt="Choose 2 Energy to put in the Lost Zone",
    )
    if picks:
        await ctx.move_to_lost_zone(picks)

async def star_requiem(ctx):
    """VSTAR Power: your opponent's Active Pokemon is Knocked Out."""
    target = ctx.defender
    if target is not None:
        await ctx.knock_out(target)

card = PokemonCardDef(
    guid="5bb2595e-f648-5396-b2c0-d1b63316590d",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaVSTAR.Name",
    display_name="Giratina VSTAR",
    searchable_by=["Giratina VSTAR", "VSTAR", "GiratinaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=69,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    family_id=487,
    abilities=[
        Attack(
            title="Lost Impact",
            game_text="Put 2 Energy attached to your Pok\u00e9mon in the Lost Zone.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=280,
            effect=lost_impact,
        ),
        Attack(
            title="Star Requiem",
            game_text="You can use this attack only if you have 10 or more cards in the Lost Zone. Your opponent's Active Pok\u00e9mon is Knocked Out. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1},
            effect=star_requiem,
            condition=lost_mine_condition,
        ),
    ],
)