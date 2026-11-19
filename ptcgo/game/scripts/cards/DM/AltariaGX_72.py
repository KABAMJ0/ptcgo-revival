from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.attributes import AttrID, SpecialConditions


async def euphoria_gx(ctx):
    """The opponent's Active is Asleep and every one of your Pokemon heals all
    damage."""
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
    for pokemon in ctx.my_pokemon_in_play():
        missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, pokemon)

card = PokemonCardDef(
    guid="a3438c01-26e5-5ba8-a58c-8437c2cbc12a",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AltariaGX.Name",
    display_name="Altaria-GX",
    searchable_by=["Altaria-GX", "Stage 1", "GX", "AltariaGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=72,
    set_code="DM",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swablu.Name",
    family_id=333,
    abilities=[
        Attack(
            title="Bright Tone",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon-GX and Pok\u00e9mon-EX.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
        Attack(
            title="Euphoria-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=euphoria_gx,
        ),
    ],
)