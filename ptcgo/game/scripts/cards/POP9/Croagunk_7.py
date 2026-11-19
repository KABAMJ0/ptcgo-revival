from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import named_in_play

async def nimble(ctx):
    """30; with Turtwig in play Croagunk heals back the damage it dealt."""
    dealt = await ctx.deal_damage(30)
    if named_in_play("Turtwig")(ctx) and ctx.attacker is not None and dealt > 0:
        await ctx.heal(dealt, ctx.attacker)

card = PokemonCardDef(
    guid="b12194de-6831-5eb5-a621-e4c010d81b06",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    display_name="Croagunk",
    searchable_by=["Croagunk", "Basic", "Croagunk"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=453,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Flip a coin. If heads, choose 1 card from your opponent's hand without looking and discard it.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Nimble",
            game_text="If you have Turtwig in play, remove from Croagunk the number of damage counters equal to the damage you did to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=nimble,
        ),
    ],
)