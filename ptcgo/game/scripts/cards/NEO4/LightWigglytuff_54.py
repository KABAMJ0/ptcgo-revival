from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for


def _evolution_names(card):
    definition = def_for(card.archetype_id)
    entry = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_FROM.value))
    return (entry or {}).get("value") or ""


def _logic_name(pokemon):
    definition = def_for(pokemon.archetype_id)
    entry = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    return (entry or {}).get("value") \
        or (getattr(definition, "display_name", "") or "").replace(" ", "")


def _evolve_card_for(card, pokemon):
    """Direct pre-evolution only: a Stage 2 must not be attached to a Basic."""
    from_name = _evolution_names(card)
    return bool(from_name) and from_name.lower() == _logic_name(pokemon).lower()


async def _evolution_song(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        in_play = ctx.session.board_state.pokemon_in_play(player_id)
        if not in_play:
            continue
        target = await ctx.choose_pokemon(
            in_play, "Choose a Pok\u00e9mon to evolve", player_id=player_id)
        if target is None:
            continue
        candidates = [card for card in ctx.deck(player_id)
                      if _evolve_card_for(card, target)]
        if not candidates:
            continue
        picks = await ctx.choose_cards(
            candidates, 1, minimum=0, player_id=player_id,
            prompt="Choose a card that evolves from that Pok\u00e9mon")
        if picks:
            await ctx.evolve_pokemon(target, picks[0])
            await ctx.shuffle_deck(player_id)


card = PokemonCardDef(
    guid="96f92ffa-33ae-55ae-868c-b26cf5f4fbca",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightWigglytuff.Name",
    display_name="Light Wigglytuff",
    searchable_by=["Light Wigglytuff", "Stage 1", "LightWigglytuff"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Evolution Song",
            game_text="Your opponent may choose 1 of his or her Pok\u00e9mon and search his or her deck for a card that evolves from that Pok\u00e9mon. Your opponent attaches that card to that Pok\u00e9mon. This counts as evolving that Pok\u00e9mon. Either way, you may do the same, and then each player who searched shuffles his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_evolution_song,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)