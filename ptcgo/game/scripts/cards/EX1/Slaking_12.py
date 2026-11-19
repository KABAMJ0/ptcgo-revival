from ptcgo.game.card_effects.passives_common import ability_lock_passive, is_in_active_spot
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _lazy_lock(pokemon, carrier):
    holder = carrier_pokemon(carrier)
    if holder is None or not is_in_active_spot(holder):
        return False
    return pokemon.owning_player_id != holder.owning_player_id


async def critical_move(ctx):
    """Discard a basic Energy attached to Slaking or this attack does nothing;
    Slaking cannot attack during your next turn."""
    from ptcgo.game.card_effects.trainers import is_basic_energy_card
    energies = [card for card in ctx.attached_energies(ctx.attacker)
                if is_basic_energy_card(card)]
    if not energies:
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=is_basic_energy_card,
        prompt="Discard a basic Energy card attached to Slaking")
    if not discarded:
        return
    await ctx.deal_damage()
    from ptcgo.game.card_effects.attacks_common import lock_all_attacks
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="05ba3cf9-5324-5441-be6f-1d585275a3db",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Slaking"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Lazy",
            game_text="As long as Slaking is your Active Pok\u00e9mon, your opponent's Pok\u00e9mon can't use any Pok\u00e9-Powers.",
            passive=ability_lock_passive(_lazy_lock),
        ),
        Attack(
            title="Critical Move",
            game_text="Discard a basic Energy card attached to Slaking or this attack does nothing. Slaking can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=critical_move,
        ),
    ],
)