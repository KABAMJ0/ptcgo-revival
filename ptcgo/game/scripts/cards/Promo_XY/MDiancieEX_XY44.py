from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import damage_shield_from

async def diamond_force(ctx):
    """Printed 100; during the opponent's next turn every friendly Pokemon takes
    no damage from the opponent's Pokemon-EX."""
    from ptcgo.game.card_effects.pokemon import is_pokemon_EX, archetype_id_of
    await ctx.deal_damage()
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_passive_through_opponents_turn(
            pokemon, damage_shield_from(lambda attacker: is_pokemon_EX(archetype_id_of(attacker))))


card = PokemonCardDef(
    guid="95586126-4fb8-5120-b2f9-fdd654e1e119",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MDiancieEX.Name",
    display_name="M Diancie-EX",
    searchable_by=["M Diancie-EX", "MEGA", "EX", "MDiancieEX"],
    subtypes=["MEGA", "EX"],
    collector_number=44,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DiancieEX.Name",
    family_id=719,
    abilities=[
        Attack(
            title="Diamond Force",
            game_text="During your opponent's next turn, prevent all damage done to each of your Pok\u00e9mon from your opponent's Pok\u00e9mon-EX. (If this Pok\u00e9mon is no longer your Active Pok\u00e9mon, this effect ends.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=diamond_force,
        ),
    ],
)