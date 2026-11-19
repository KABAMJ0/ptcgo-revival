import json

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.attacks_common import (
    _evolve_from_deck_candidates, flip_gate,
)
from ptcgo.game.card_effects.pokemon import energy_provides_type


def _printed_types(card):
    """A deck card's Pokemon types live on its definition, not the entity."""
    definition = def_for(card.archetype_id)
    spec = (getattr(definition, "extra_attributes", {}) or {}).get(
        str(AttrID.POKEMON_TYPES.value))
    raw = spec.get("value") if isinstance(spec, dict) else None
    if isinstance(raw, str):
        raw = json.loads(raw or "[]")
    return set(raw or [])


async def energy_evolution(ctx):
    holder = ctx.energy_receiver
    if holder is None or ctx.source is None:
        return
    if holder.entity_id != ctx.source.entity_id:
        return
    energy = ctx.attached_energy
    if energy is None:
        return
    types = {pokemon_type.value for pokemon_type in PokemonTypes
             if energy_provides_type(energy, pokemon_type.value)}
    candidates = [
        card for card in _evolve_from_deck_candidates(
            ctx, holder,
            lambda card: bool(_printed_types(card) & types))
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0, prompt="Choose an Evolution card")
    if not picks:
        return
    await ctx.evolve_pokemon(holder, picks[0])
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="b104486b-87e1-5fd4-b3fd-76ba92760d81",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Energy Evolution",
            game_text="When you attach a basic Energy card from your hand to this Pok\u00e9mon during your turn, you may search your deck for a card that evolves from this Pok\u00e9mon that is the same type as that Energy card and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=energy_evolution,
        ),
        Attack(
            title="Quick Draw",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=draw_attack(1)),
        ),
    ],
)