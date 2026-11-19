from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def life_drain(ctx):
    """Heads: put damage counters on the Defending Pokemon until it is 10 HP away
    from being Knocked Out."""
    results = await ctx.flip_coins(1, "Life Drain")
    if not (results and results[0]):
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    remaining = defender.get_attribute(AttrID.HP, 0)
    if remaining <= 10:
        return
    await ctx.deal_damage(remaining - 10, apply_modifiers=False, as_counters=True)

card = PokemonCardDef(
    guid="a8d1be09-1a17-533e-80e0-8a99d0131922",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    display_name="Kirlia",
    searchable_by=["Kirlia", "Stage 1", "Kirlia"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ralts.Name",
    family_id=280,
    abilities=[
        Attack(
            title="Dazzle Dance",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Life Drain",
            game_text="Flip a coin. If heads, put damage counters on the Defending Pok\u00e9mon until it is 10 HP away from being Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=life_drain,
        ),
    ],
)