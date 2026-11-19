from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.attacks_common import lock_defender_attacks
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _heal_own_bench(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="af8d4c0e-3c41-5d66-9e1d-865d441b0793",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Cleanse Away",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=_heal_own_bench,
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)