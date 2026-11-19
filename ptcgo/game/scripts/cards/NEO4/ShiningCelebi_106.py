from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _healing_water(ctx):
    if ctx.attacker is None:
        return
    water = sum(1 for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.WATER.value))
    bench = [pokemon for pokemon in ctx.my_bench()
             if pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon)]
    if water <= 0 or not bench:
        return
    pick = await ctx.choose_pokemon(bench, "Choose a Benched Pok\u00e9mon to heal")
    if pick is not None:
        await ctx.heal(10 * water, pick)


async def _miracle_leaf(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    coins = len(ctx.attached_energies(defender))
    if coins <= 0:
        return
    results = await ctx.flip_coins(coins, "Miracle Leaf")
    if not any(results):
        return
    conditions = [SpecialConditions.ASLEEP, SpecialConditions.CONFUSED,
                  SpecialConditions.POISONED]
    index = await ctx.choose("Choose a Special Condition",
                             ["Asleep", "Confused", "Poisoned"])
    await ctx.apply_special_condition(defender, conditions[index])


card = PokemonCardDef(
    guid="fb104cfa-034b-512e-9601-0fc5fdd76d14",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCelebi.Name",
    display_name="Shining Celebi",
    searchable_by=["Shining Celebi", "Basic", "ShiningCelebi"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Healing Water",
            game_text="Remove a number of damage counters from 1 of your Benched Pok\u00e9mon equal to the number of Water Energy cards attached to Shining Celebi. If the Pok\u00e9mon has fewer damage counters than that, remove all of them.",
            cost={PokemonTypes.WATER: 1},
            effect=_healing_water,
        ),
        Attack(
            title="Miracle Leaf",
            game_text="Flip a number of coins equal to the number of Energy attached to the Defending Pok\u00e9mon. If you get 1 or more heads, the Defending Pok\u00e9mon is now Asleep, Confused, or Poisoned (your choice).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=_miracle_leaf,
        ),
    ],
)