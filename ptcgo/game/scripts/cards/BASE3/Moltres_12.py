from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _wildfire(ctx):
    """Discard any number of Fire Energy cards attached to this Pokemon; if you
    do, discard that many cards from the top of your opponent's deck."""
    attacker = ctx.attacker
    if attacker is None:
        return
    fire = [energy for energy in ctx.attached_energies(attacker)
            if energy_provides_type(energy, PokemonTypes.FIRE.value)]
    if not fire:
        return
    picked = await ctx.choose_cards(
        fire, len(fire), minimum=0,
        prompt="Choose any number of Fire Energy to discard")
    if not picked:
        return
    await ctx.discard_cards(picked)
    milled = ctx.deck_top(len(picked), player_id=ctx.opponent_id)
    if milled:
        await ctx.discard_cards(milled)

card = PokemonCardDef(
    guid="5c184cf3-6cdd-5cb8-971e-7fd55fc0dbf1",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
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
            effect=_wildfire,
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