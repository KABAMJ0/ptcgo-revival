from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import opponent_switches


async def _opponent_switches_after_damage(ctx):
    """Printed damage, then the opponent picks their new Active."""
    await ctx.deal_damage()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="093b99c3-a8df-511f-acc4-a9d88a7889b8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    display_name="Whismur",
    searchable_by=["Whismur", "Basic", "Whismur"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=293,
    abilities=[
        Attack(
            title="Wail",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=_opponent_switches_after_damage,
        ),
    ],
)