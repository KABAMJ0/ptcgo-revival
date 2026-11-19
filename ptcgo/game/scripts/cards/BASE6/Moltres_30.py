from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

_is_fire_energy = basic_energy_of("fire")


async def wildfire(ctx):
    """Optional discard of any number of Fire Energy on Moltres, then mill
    that many cards off the top of the opponent's deck."""
    attacker = ctx.attacker
    if attacker is None:
        return
    fires = [card for card in ctx.attached_energies(attacker)
             if _is_fire_energy(card)]
    if not fires:
        return
    picked = await ctx.choose_cards(
        fires, len(fires), minimum=0,
        prompt="Discard any number of Fire Energy cards")
    if not picked:
        return
    await ctx.discard_cards(picked)
    milled = ctx.deck_top(len(picked), player_id=ctx.opponent_id)
    if milled:
        await ctx.discard_cards(milled)


card = PokemonCardDef(
    guid="360e2e0d-1030-5123-addc-d285e3ef9f85",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BASE6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Wildfire",
            game_text="You may discard any number of Fire Energy cards attached to Moltres when you use this attack. If you do, discard that many cards from the top of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=wildfire,
        ),
        Attack(
            title="Dive Bomb",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 4},
            damage=80,
            effect=flip_or_nothing(),
        ),
    ],
)