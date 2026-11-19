from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import opponent_switches


async def _opponent_switches_after_damage(ctx):
    """Printed damage, then the opponent picks their new Active."""
    await ctx.deal_damage()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="64076c72-2383-52e0-b978-0480c9536618",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic", "Yamper"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_opponent_switches_after_damage,
        ),
        Attack(
            title="Static Shock",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)