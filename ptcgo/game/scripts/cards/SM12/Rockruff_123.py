from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import opponent_switches


async def _opponent_switches_after_damage(ctx):
    """Printed damage, then the opponent picks their new Active."""
    await ctx.deal_damage()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="19adfc95-a6b3-5430-9b3f-2638500a89b6",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    display_name="Rockruff",
    searchable_by=["Rockruff", "Basic", "Rockruff"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=744,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_opponent_switches_after_damage,
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)