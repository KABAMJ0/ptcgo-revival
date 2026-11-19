from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.card_effects.passives_common import apply_protection
async def stardust(ctx):
    """Printed 10; discard a Special Energy from the opponent's Active, and if
    one was discarded prevent all attack effects and damage through their turn."""
    from ptcgo.game.attributes import AttrID as _Attr
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    specials = [e for e in ctx.attached_energies(defender)
                if e.get_attribute(_Attr.IS_SPECIAL_ENERGY)]
    if not specials:
        return
    picked = await ctx.choose_cards(specials, 1, prompt="Discard a Special Energy")
    if not picked:
        return
    await ctx.discard_cards(picked)
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="7456444a-ae0f-5b2d-92cc-7133ef47e477",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Attack(
            title="Stardust",
            game_text="Discard a Special Energy attached to your opponent's Active Pok\u00e9mon. If you do, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=stardust,
        ),
        Attack(
            title="Dream Dance",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)