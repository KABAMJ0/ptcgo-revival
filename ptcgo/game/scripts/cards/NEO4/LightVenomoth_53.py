from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, def_for
from ptcgo.game.card_effects.attacks_common import bonus_if


def _is_pokemon_card(card):
    return isinstance(def_for(card.archetype_id), PokemonCardDef)


def _same_energy_count(ctx):
    defender, attacker = ctx.defender, ctx.attacker
    if defender is None or attacker is None:
        return False
    return len(ctx.attached_energies(defender)) == len(ctx.attached_energies(attacker))


async def _mysterious_wing(ctx):
    for player_id in (ctx.opponent_id, ctx.player_id):
        pile = [card for card in ctx.discard_pile(player_id) if _is_pokemon_card(card)]
        if not pile:
            continue
        picks = await ctx.choose_cards(
            pile, 1, minimum=0, player_id=player_id,
            prompt="Choose a Pok\u00e9mon card from your discard pile")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="59f26242-3595-5aed-bb8f-15081d8e5f9d",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightVenomoth.Name",
    display_name="Light Venomoth",
    searchable_by=["Light Venomoth", "Stage 1", "LightVenomoth"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Mysterious Wing",
            game_text="Your opponent may choose a Baby Pok\u00e9mon, Basic Pok\u00e9mon, or Evolution card from his or her discard pile and put it into his or her hand. Either way, you may do the same.",
            cost={PokemonTypes.GRASS: 1},
            effect=_mysterious_wing,
        ),
        Attack(
            title="Synchronize",
            game_text="If Light Venomoth and the Defending Pok\u00e9mon have a different number of Energy cards attached to them, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=bonus_if(_same_energy_count, 0, base=40, else_nothing=True),
        ),
    ],
)