from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

import json

from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.support_common import is_basic

def _basic_types(card):
    definition = def_for(card.archetype_id)
    spec = (getattr(definition, "extra_attributes", {}) or {}).get(
        str(AttrID.POKEMON_TYPES.value))
    raw = spec.get("value") if isinstance(spec, dict) else None
    if isinstance(raw, str):
        raw = json.loads(raw or "[]")
    return set(raw or [])


async def rally(ctx):
    """Up to one Basic Pokemon of each of three different types onto the Bench."""
    basics = [card for card in ctx.deck() if is_basic(card)]
    by_type = {}
    for card in basics:
        for type_value in _basic_types(card):
            by_type.setdefault(type_value, []).append(card)
    if not by_type:
        return
    slots = list(by_type.items())[:3]
    picked = await ctx.search_deck_groups(
        [(lambda card, cards=cards: card in cards, 1, "Type %d" % type_value)
         for type_value, cards in slots],
        "Search your deck for up to 3 different types of Basic Pokemon")
    cards = [card for group in picked for card in group]
    for card in cards:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="a4f7ea18-485f-55e9-b139-5916269d078e",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="POP7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Rally",
            game_text="Search your deck for up to 3 different types of Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rally,
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)