from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.content.definitions import Triggers
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _flying_beatdown(ctx):
    """Discard a Grass AND a Fighting Energy from itself; only then is the
    Defending Pokemon Paralyzed."""
    attacker = ctx.attacker
    if attacker is None:
        return
    grass = fighting = None
    for energy in ctx.attached_energies(attacker):
        types = energy.get_attribute(AttrID.POKEMON_TYPES) or []
        if grass is None and PokemonTypes.GRASS.value in types:
            grass = energy
        elif fighting is None and PokemonTypes.FIGHTING.value in types:
            fighting = energy
    if grass is None or fighting is None:
        return
    await ctx.discard_cards([grass, fighting])
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="7fdf7938-e0ac-59f8-872b-19d8ce42d277",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=53,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=330,
    abilities=[
        Ability(
            title="Sand Slammer",
            game_text="At any time between turns, if this Pok\u00e9mon is your Active Pok\u00e9mon, put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            trigger=Triggers.BETWEEN_TURNS,
            condition=lambda board, player_id, pokemon: is_in_active_spot(pokemon),
            effect=place_counters(1, target="each_opponent"),
        ),
        Attack(
            title="Flying Beatdown",
            game_text="You may discard a Grass Energy and a Fighting Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_flying_beatdown,
        ),
    ],
)