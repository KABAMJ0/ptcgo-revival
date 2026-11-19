from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.pokemon import devolve_depth
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def devolution_beam(ctx):
    results = await ctx.flip_coins(1, "Devolution Beam")
    if not (results and results[0]):
        return
    candidates = [pokemon for pokemon in list(ctx.my_pokemon_in_play())
                  + list(ctx.opponent_pokemon_in_play()) if devolve_depth(pokemon) > 0]
    if not candidates:
        return
    target = candidates[0] if len(candidates) == 1 else await ctx.choose_pokemon(
        candidates, "Choose an Evolved Pokémon")
    if target is None:
        return
    await ctx.devolve_pokemon(target, steps=1, destination="hand")

card = PokemonCardDef(
    guid="a9f56ea5-9718-5dc3-99c9-2c97a104a3ba",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Psywave",
            game_text="Does 10 damage times the amount of Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_energy("defender"), 10),
        ),
        Attack(
            title="Devolution Beam",
            game_text="Flip a coin. If heads, choose 1 of either player's Evolved Pok\u00e9mon, remove the highest stage Evolution card from that Pok\u00e9mon, and put it into that player's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=devolution_beam,
        ),
    ],
)