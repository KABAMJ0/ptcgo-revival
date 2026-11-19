import json

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.content.definitions import def_for, evolves_from_chain
from ptcgo.game.session.passives import is_basic_energy


def _printed_types(card):
    definition = def_for(card.archetype_id)
    spec = (getattr(definition, "extra_attributes", {}) or {}).get(
        str(AttrID.POKEMON_TYPES.value))
    value = spec.get("value") if isinstance(spec, dict) else spec
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except ValueError:
            return set()
    return set(value or [])


async def _energy_evolution(ctx):
    energy = getattr(ctx, "attached_energy", None)
    if energy is None or getattr(ctx, "energy_receiver", None) is not ctx.source:
        return
    if not is_basic_energy(energy):
        return
    provided = {member.value for member in PokemonTypes
                if energy_provides_type(energy, member.value)}
    holder = def_for(ctx.source.archetype_id)
    mine = (getattr(holder, "display_name", "") or "").lower()
    if not provided or not mine:
        return
    options = [card for card in ctx.deck()
               if mine in [str(name).lower()
                           for name in (evolves_from_chain(card.archetype_id) or [])]
               and _printed_types(card) & provided]
    if not options:
        return
    if not await ctx.ask_yes_no(
            "Search your deck for a card to evolve this Pok\u00e9mon?"):
        return
    picks = await ctx.choose_cards(
        options, 1, minimum=1,
        prompt="Choose a card that evolves this Pok\u00e9mon")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="29e3a442-986c-5ab7-a914-588814ff1a63",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SM1",
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
            effect=_energy_evolution,
        ),
        Attack(
            title="Quick Draw",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=draw_attack(1)),
        ),
    ],
)