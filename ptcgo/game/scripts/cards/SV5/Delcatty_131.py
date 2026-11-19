from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


async def regal_blender(ctx):
    """Printed damage, then you may move any amount of Energy between your
    Pokémon in any way you like."""
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    if len(mine) > 1 and await ctx.ask_yes_no(
        "Move any amount of Energy from your Pokémon to your other Pokémon?"
    ):
        await ctx.move_energy_freely(mine, mine)


card = PokemonCardDef(
    guid="d96b3bf9-6f39-5acb-88ff-de44e8b5d5cd",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Energy Blender",
            game_text="You may move any amount of Energy from your Pok\u00e9mon to your other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=regal_blender,
        ),
    ],
)