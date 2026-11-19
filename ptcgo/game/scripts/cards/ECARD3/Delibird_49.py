from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.trainers import is_tool_card
from ptcgo.game.data_utils import def_for


def _is_tm_or_tool(card):
    if is_tool_card(card):
        return True
    name = (getattr(def_for(card.archetype_id), "display_name", "") or "").lower()
    return "technical machine" in name


async def _limited_delivery(ctx):
    found = await ctx.search_deck(
        _is_tm_or_tool, count=1, minimum=0,
        prompt="Search your deck for a Technical Machine or Pokémon Tool card")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="97445aa1-48cf-50a6-904c-b9e715735cb7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Limited Delivery",
            game_text="Search your deck for a Technical Machine or Pok\u00e9mon Tool card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_limited_delivery,
        ),
        Attack(
            title="Kick Away",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)