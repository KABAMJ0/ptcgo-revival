from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import opponent_switches


async def crystal_wave(ctx):
    """Printed 30; heads adds 10, tails lets the opponent switch their Active."""
    heads = await ctx.flip_coins(1, "Crystal Wave")
    if heads and heads[0]:
        await ctx.deal_damage(40)
    else:
        await ctx.deal_damage(30)
        await opponent_switches(ctx)

card = PokemonCardDef(
    guid="5262e0e0-63cf-551f-97f8-c9a2c8cb6ebd",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Legendary Body",
            game_text="As long as Suicune is your Active Pok\u00e9mon, Suicune and Energy cards attached to it aren't affected by effects from Trainer cards other than Stadium cards. As long as this Power is active, discard any Trainer cards attached to Suicune. (This power works even if Suicune is Asleep, Confused, or Paralyzed.)",
            effect=unimplemented,
        ),
        Attack(
            title="Crystal Wave",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage. If tails, this attack does 30 damage and, if your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches it with the Defending Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            damage_operator="+",
            effect=crystal_wave,
        ),
    ],
)