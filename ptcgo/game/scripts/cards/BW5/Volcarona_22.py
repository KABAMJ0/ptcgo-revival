from ptcgo.game.card_effects.passives_common import BurnCountersPassive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _burning_wind(ctx):
    """Printed 70; you may discard an Energy from this Pokemon, and if you do
    the Defending Pokemon is Burned."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    if not energies:
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=0,
        prompt="Discard an Energy from this Pokemon?")
    if not picked:
        return
    await ctx.discard_cards(picked)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.apply_special_condition(defender, SpecialConditions.BURNED)


card = PokemonCardDef(
    guid="0b1c021e-6322-5075-bb77-d208613b35a7",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Scorching Scales",
            game_text="Put 4 damage counters instead of 2 on your opponent's Burned Pok\u00e9mon between turns.",
            passive=BurnCountersPassive(4),
        ),
        Attack(
            title="Burning Wind",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_burning_wind,
        ),
    ],
)