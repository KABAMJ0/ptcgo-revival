from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ripping_horn(ctx):
    results = await ctx.flip_coins(3, "Ripping Horn")
    heads = sum(1 for r in results if r)
    if heads == 0:
        return
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_energy_from(
        target, heads,
        prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="507d6af5-a0a8-583f-81ee-d3c24b493b42",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="ME55",
    rarity=Rarities.Common,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Three-Headed Bite",
            game_text="Flip 3 coins. For each heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ripping_horn,
        ),
        Attack(
            title="Pitch-Black Fangs",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)