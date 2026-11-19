from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot


async def _synchronized_feathers(ctx):
    await ctx.deal_damage()
    if is_in_active_spot(ctx.source):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    picks = bench if len(bench) == 1 else await ctx.choose_cards(
        bench, 1, minimum=0,
        prompt="Choose 1 of your opponent's Benched Pok\u00e9mon")
    for target in picks:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="b93e712d-8b5d-57d4-bba1-d7e6e79ae04d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic", "Flamigo"],
    subtypes=["Basic"],
    collector_number=185,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=973,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Synchronized Feathers",
            game_text="If Flamigo is on your Bench, this attack also does 60 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_synchronized_feathers,
        ),
    ],
)