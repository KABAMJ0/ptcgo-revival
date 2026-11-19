from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import flip_gate


async def aerowing(ctx):
    """You may flip: heads doubles the printed 40 to 80, tails does nothing."""
    if not await ctx.ask_yes_no("Flip a coin for Aerowing?"):
        await ctx.deal_damage()
        return
    heads = await ctx.flip_coins(1, "Aerowing")
    if heads and heads[0]:
        await ctx.deal_damage(80)

card = PokemonCardDef(
    guid="b8503fed-f8fd-5b3c-8275-b16fd2564bc9",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Attack(
            title="Aerowing",
            game_text="You may flip a coin. If heads, this attack does 80 damage. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            effect=aerowing,
        ),
    ],
)