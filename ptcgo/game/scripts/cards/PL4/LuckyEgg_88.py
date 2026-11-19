from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities


async def lucky_egg_ko_effect(ctx):
    """Holder Knocked Out by damage from an opponent's attack: draw until 7."""
    if not ctx.ko_from_attack:
        return
    await ctx.draw_until(7)


card = PokemonToolCardDef(
    guid="14a7695d-ff54-5e94-bbfa-f1dbfed733a1",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyEgg.Name",
    display_name="Lucky Egg",
    searchable_by=["Lucky Egg", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=88,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Lucky Egg",
            game_text="When the Pok\u00e9mon this card is attached to is Knocked Out by damage from an opponent's attack, draw cards until you have 7 cards in your hand.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=lucky_egg_ko_effect,
        ),
    ],
)
