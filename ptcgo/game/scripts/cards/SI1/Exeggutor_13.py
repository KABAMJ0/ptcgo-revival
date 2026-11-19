from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def sharpshooter(ctx):
    coins = count_energy("self", PokemonTypes.GRASS)(ctx)
    results = await ctx.flip_coins(coins, "Sharpshooter") if coins else []
    heads = sum(1 for result in results if result)
    if heads <= 0:
        return 0
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(),
        "Choose 1 of your opponent's Pokémon.",
    )
    if target is None:
        return 0
    return await ctx.deal_damage(heads * 10, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="9d21a85d-4539-5f7f-9180-34d94424bebe",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=103,
    abilities=[
        Attack(
            title="Sharpshooter",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Flip a number of coins equal to the number of Grass Energy attached to Exeggutor. This attack does 10 damage times the number of heads to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.GRASS: 1},
            effect=sharpshooter,
        ),
    ],
)