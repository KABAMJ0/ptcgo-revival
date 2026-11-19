from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented


async def _power_pinch(ctx):
    """One Energy off the Defending Pokemon per head."""
    results = await ctx.flip_coins(2, "Power Pinch")
    heads = sum(1 for r in results if r)
    defender = ctx.defender
    if heads <= 0 or defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(defender, heads,
                                  prompt="Choose Energy to discard from the Defending Pok\u00e9mon")
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="6f513721-8cb4-5951-9c5a-e622e7f9167a",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Power Pinch",
            game_text="Flip 2 coins. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_power_pinch,
        ),
        Attack(
            title="Grip and Squeeze",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=no_retreat_attack(),
        ),
    ],
)