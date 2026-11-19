from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def selfdestruct(ctx):
    """Printed 80, then 20 to every Benched Pokemon on both sides (no Weakness
    or Resistance), then 80 to Magneton itself."""
    await ctx.deal_damage()
    for pid in (ctx.player_id, ctx.opponent_id):
        for pokemon in ctx.board.find_player_area(pid, "bench").children:
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)
    await ctx.deal_damage(80, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="e6477402-2da2-56ee-af38-59e2105d0494",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    display_name="Magneton",
    searchable_by=["Magneton", "Stage 1", "Magneton"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BASE4",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Selfdestruct",
            game_text="Does 20 damage to each player's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Magneton does 80 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=selfdestruct,
        ),
    ],
)