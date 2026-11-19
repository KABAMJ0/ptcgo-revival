from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def cross_attack(ctx):
    """Four coins: 20 per heads, and Confused at 2 or more."""
    flips = await ctx.flip_coins(4, "Cross Attack")
    heads = sum(1 for flip in flips if flip)
    if heads:
        await ctx.deal_damage(20 * heads)
    if heads >= 2:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)

card = PokemonCardDef(
    guid="619a95eb-659d-5477-a8e4-fec142f22374",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Triggered Poison",
            game_text="If your opponent attaches an Energy card to the Defending Pok\u00e9mon during his or her next turn, that Pok\u00e9mon becomes Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Cross Attack",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads. If you get 2 or more heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=cross_attack,
        ),
    ],
)