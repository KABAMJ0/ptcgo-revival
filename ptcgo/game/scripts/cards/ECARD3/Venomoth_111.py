from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.trainers import choose_condition_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _healing_dust(ctx):
    results = await ctx.flip_coins(2, "Healing Dust")
    heads = sum(1 for result in results if result)
    if not heads:
        return
    for pokemon in ctx.my_pokemon_in_play():
        await ctx.heal(10 * heads, pokemon)


card = PokemonCardDef(
    guid="bc4b25cd-3159-569f-83a2-7e53556dd550",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=111,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Healing Dust",
            game_text="Flip 2 coins. For each heads, remove 1 damage counter from each of your Pok\u00e9mon. If a Pok\u00e9mon has fewer damage counters than the number of heads, remove all of them.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_healing_dust,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition (Asleep, Burned, Confused, Paralyzed, or Poisoned). The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=composed(lambda ctx: ctx.deal_damage(30), flip_gate(choose_condition_attack())),
        ),
    ],
)