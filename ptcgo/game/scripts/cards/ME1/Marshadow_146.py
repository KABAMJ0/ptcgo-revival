from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import shield_source_next_turn


async def shadowy_side_kick(ctx):
    """60; if that Knocked something Out, shield this Pokemon from all damage
    and effects of attacks through the opponent's next turn."""
    await ctx.deal_damage()
    if ctx.knockouts:
        await shield_source_next_turn(prevent=True, effects_too=True)(ctx)


card = PokemonCardDef(
    guid="b1c36586-a79f-56a4-bfbb-9bd817a391d2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marshadow.Name",
    display_name="Marshadow",
    searchable_by=["Marshadow", "Basic", "Marshadow"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=802,
    abilities=[
        Attack(
            title="Shadowy Side Kick",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from this attack, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=shadowy_side_kick,
        ),
    ],
)