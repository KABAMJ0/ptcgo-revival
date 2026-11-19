from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _heal_own_bench(ctx):
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(100, pokemon)


card = PokemonCardDef(
    guid="e85ec9b5-2407-575d-8e02-a451816df6b1",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeonex.Name",
    display_name="Leafeon ex",
    searchable_by=["Leafeon ex", "Stage 1", "Tera", "ex", "Leafeonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=6,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Verdant Storm",
            game_text="This attack does 60 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 60),
        ),
        Attack(
            title="Moss Agate",
            game_text="Heal 100 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=230,
            effect=_heal_own_bench,
        ),
    ],
)