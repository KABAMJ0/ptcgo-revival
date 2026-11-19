from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.card_effects.attacks_common import mill_attack


def _has_bug_out(card) -> bool:
    definition = def_for(card.archetype_id)
    return any(getattr(ability, "title", "") == "Bug Out"
               for ability in getattr(definition, "abilities", []) or [])


async def bug_out(ctx):
    """Reveal the bottom 7 cards: 50 per Pokemon there with the Bug Out
    attack; the revealed Pokemon go back into the deck, the rest are
    discarded."""
    bottom = ctx.deck(ctx.player_id)[:7]
    if not bottom:
        return
    await ctx.reveal_cards(bottom)
    count = sum(1 for card in bottom if _has_bug_out(card))
    if count:
        await ctx.deal_damage(50 * count)
    pokemon = [card for card in bottom if is_pokemon_card(card)]
    if pokemon:
        await ctx.shuffle_into_deck(pokemon, ctx.player_id)
    others = [card for card in bottom if card not in pokemon]
    if others:
        await ctx.discard_cards(others)


card = PokemonCardDef(
    guid="0c1dc4c8-1b57-5eca-bd03-32a2a2e04d8a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic", "Sizzlipede"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Controlled Burn",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=mill_attack(1),
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pok\u00e9mon you find there that has the Bug Out attack. Then, shuffle any revealed Pok\u00e9mon back into your deck. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=bug_out,
        ),
    ],
)