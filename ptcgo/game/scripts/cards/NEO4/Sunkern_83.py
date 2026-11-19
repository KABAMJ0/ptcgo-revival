from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import def_for


def _logic_name(pokemon):
    definition = def_for(pokemon.archetype_id)
    entry = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_NAME.value))
    return (entry or {}).get("value") \
        or (getattr(definition, "display_name", "") or "").replace(" ", "")


def _evolve_card_for(card, pokemon):
    """Direct pre-evolution only: a Stage 2 must not be attached to a Basic."""
    definition = def_for(card.archetype_id)
    entry = definition.extra_attributes.get(str(AttrID.EVOLUTION_LOGIC_FROM.value))
    from_name = (entry or {}).get("value") or ""
    return bool(from_name) and from_name.lower() == _logic_name(pokemon).lower()


async def _attach_evolution_sunbathe(ctx):
    results = await ctx.flip_coins(1, "Sunbathe")
    if not (results and results[0]):
        return
    attacker = ctx.attacker
    if attacker is not None:
        await ctx.heal(ctx.max_hp(attacker), attacker)
        candidates = [card for card in ctx.deck()
                      if _evolve_card_for(card, attacker)]
        if candidates:
            picks = await ctx.choose_cards(
                candidates, 1, minimum=0,
                prompt="Choose a card that evolves from Sunkern")
            if picks:
                await ctx.evolve_pokemon(attacker, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="26a0f82e-d3c1-5b2f-afaf-0db26a40f5db",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    display_name="Sunkern",
    searchable_by=["Sunkern", "Basic", "Sunkern"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=191,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sunbathe",
            game_text="Flip a coin. If heads, remove all damage counters from Sunkern. Search your deck for a card that evolves from Sunkern and attach that card to Sunkern. This counts as evolving Sunkern. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 2},
            effect=_attach_evolution_sunbathe,
        ),
    ],
)