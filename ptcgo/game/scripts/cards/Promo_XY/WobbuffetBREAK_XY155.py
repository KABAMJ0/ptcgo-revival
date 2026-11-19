from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon

class RightBackAtYouPassive(Passive):
    """Counter-counters equal to the damage an attack just dealt to the carrier."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier_pokemon(carrier):
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def right_back_at_you(ctx):
    """Discard all Energy from this Pokemon, then counter the damage it takes
    during the opponent's next turn."""
    await ctx.discard_energy_from(ctx.attacker, 99,
                                  prompt="Choose Energy to discard from this Pokemon")
    ctx.add_passive_through_opponents_turn(ctx.attacker, RightBackAtYouPassive())


card = PokemonCardDef(
    guid="cfa6326d-5738-5944-bcd1-05c9dec05ad1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WobbuffetBREAK.Name",
    display_name="Wobbuffet BREAK",
    searchable_by=["Wobbuffet BREAK", "BREAK", "WobbuffetBREAK"],
    subtypes=["BREAK"],
    collector_number=155,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    family_id=202,
    abilities=[
        Attack(
            title="Right Back at You",
            game_text="Discard all Energy attached to this Pok\u00e9mon. During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=right_back_at_you,
        ),
    ],
)