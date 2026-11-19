from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.data_utils import Triggers


async def bolt(ctx):
    """Whenever an opponent's attack damages Entei without Knocking it Out,
    flip a coin: on heads shuffle Entei and everything attached into the deck."""
    heads = await ctx.flip_coins(1, "Bolt")
    if not heads or not heads[0]:
        return
    await remove_self_from_play(destination="deck")(ctx)

card = PokemonCardDef(
    guid="6fffe00a-c089-5367-b118-dfaaa744ad49",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Bolt",
            game_text="Whenever your opponent's attack damages Entei, unless that attack Knocks Out Entei, flip a coin. If heads, shuffle Entei and all cards attached to it into your deck. This power can't be used if Entei is already Asleep, Confused, or Paralyzed when it is damaged.",
            effect=bolt,
        ),
        Attack(
            title="Protective Flame",
            game_text="During your opponent's next turn, prevent all effects of attacks, including damage, done to your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)