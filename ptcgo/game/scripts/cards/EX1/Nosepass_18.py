from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.pokemon import devolve_depth, is_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _evolved_opponent_active(ctx):
    active = ctx.opponent_active()
    return active is not None and devolve_depth(active) > 0


async def invisible_hand(ctx):
    if not _evolved_opponent_active(ctx):
        return
    await search_to_hand(count=1, reveal=False,
                         prompt="Search your deck for any 1 card")(ctx)


async def repulsion(ctx):
    results = await ctx.flip_coins(1, "Repulsion")
    if not (results and results[0]):
        return
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.put_in_hand([defender], reveal=True)

card = PokemonCardDef(
    guid="b8e539b2-db4a-5b64-8b4b-cdccb63ac4c4",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=299,
    abilities=[
        Attack(
            title="Invisible Hand",
            game_text="If any of your opponent's Active Pok\u00e9mon are Evolved Pok\u00e9mon, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=invisible_hand,
        ),
        Attack(
            title="Repulsion",
            game_text="Flip a coin. If heads, your opponent returns the Defending Pok\u00e9mon and all cards attached to it to his or her hand. (If your opponent doesn't have any Benched Pok\u00e9mon or other Active Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=repulsion,
        ),
    ],
)