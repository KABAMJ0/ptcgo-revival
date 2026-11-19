from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import AttrID


async def _bind_wound(ctx):
    results = await ctx.flip_coins(1, "Bind Wound")
    if not (results and results[0]):
        return
    damaged = [p for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    target = damaged[0] if len(damaged) == 1 else await ctx.choose_pokemon(
        damaged, "Choose a Pokémon to remove damage counters from")
    if target is not None:
        await ctx.heal(20, target)


async def _dogpile(ctx):
    benched = len(ctx.my_bench())
    if benched <= 0:
        return
    await ctx.deal_damage(10 * benched)
    await ctx.deal_damage(10 * benched, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="1705fe3b-79a4-5b19-8330-ee61235b8596",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Flip a coin. If heads, remove 2 damage counters from 1 of your Pok\u00e9mon (1 if it has only 1).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_bind_wound,
        ),
        Attack(
            title="Dogpile",
            game_text="Count the number of Pok\u00e9mon on your Bench. This attack does 10 times that number of damage to the Defending Pok\u00e9mon, and Chansey does 10 times that number of damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="x",
            effect=_dogpile,
        ),
    ],
)