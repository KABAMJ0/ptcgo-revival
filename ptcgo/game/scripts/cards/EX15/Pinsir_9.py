from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


async def _delta_call(ctx):
    picks = await ctx.search_deck(
        _is_delta, count=1, minimum=0,
        prompt="Choose a Pok\u00e9mon that has \u03b4 on its card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def _is_delta(card):
    name = getattr(def_for(card.archetype_id), "display_name", "") or ""
    return "\u03b4" in name


card = PokemonCardDef(
    guid="8f037289-0e10-5ced-8b61-4cfc77e89658",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir δ",
    searchable_by=["Pinsir \u03b4", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Ability(
            title="Armor",
            game_text="If your opponent has 5 of more cards in his or her hand, any damage done to Pinsir by attacks is reduced by 30 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Delta Call",
            game_text="Search your deck for a Pok\u00e9mon that has \u03b4 on its card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_delta_call,
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)