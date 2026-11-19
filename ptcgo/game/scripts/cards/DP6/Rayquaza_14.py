from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _fire_or_lightning_energy(card) -> bool:
    return (energy_provides_type(card, PokemonTypes.FIRE.value)
            or energy_provides_type(card, PokemonTypes.LIGHTNING.value))


def _speed_gain_condition(board, player_id, pokemon) -> bool:
    """A clean Rayquaza with no second Rayquaza in play and a targetable Energy."""
    if not unafflicted(board, player_id, pokemon):
        return False
    for other in board.pokemon_in_play(player_id):
        if other is not pokemon and other.get_attribute(
                AttrID.EVOLUTION_LOGIC_NAME) == "Rayquaza":
            return False
    discard = board.find_player_area(player_id, "discard")
    return any(_fire_or_lightning_energy(card)
               for card in (discard.children if discard else []))


async def _speed_gain(ctx):
    heads = await ctx.flip_until_tails("Speed Gain")
    if heads <= 0:
        return
    pool = [card for card in ctx.discard_pile() if _fire_or_lightning_energy(card)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, heads, minimum=0,
        prompt=f"Choose up to {heads} basic Fire or Lightning Energy cards to attach")
    for card in picks:
        await ctx.attach_energy(card, ctx.source)

card = PokemonCardDef(
    guid="a4f643a1-2861-5245-9568-0da363d05191",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Ability(
            title="Speed Gain",
            game_text="Once during your turn (before your attack), you may flip a coin until you get tails. For each heads, search your discard pile for a basic Fire Energy card or a basic Lightning Energy card and attach it to Rayquaza. This power can't be used if Rayquaza is affected by a Special Condition or if you have another Rayquaza in play.",
            activation=Activations.ONCE_PER_TURN,
            condition=_speed_gain_condition,
            effect=_speed_gain,
        ),
        Attack(
            title="Sky Judgement",
            game_text="Discard all Energy attached to Rayquaza.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 2},
            damage=150,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)