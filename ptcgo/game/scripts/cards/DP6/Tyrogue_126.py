from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.models.board import PokemonEntity
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.effects import full_stack
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.attributes import SpecialConditions, AttrID

_baby_effect, _baby_in_hand = baby_evolution("Hitmonlee", "Hitmonchan", "Hitmontop")


async def _gut_blow(ctx):
    """Gut Blow: +20 and 10 to itself when the Defending Pokemon is Evolved."""
    defender = ctx.defender
    evolved = defender is not None and any(
        isinstance(child, PokemonEntity)
        for child in getattr(defender, "children", []) or [])
    await ctx.deal_damage(30 if evolved else 10)
    if evolved and ctx.attacker is not None:
        await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)


async def _gut_blow(ctx):
    """Gut Blow: +20 and 10 to itself when the Defending Pokemon is Evolved."""
    defender = ctx.defender
    evolved = defender is not None and any(
        isinstance(child, PokemonEntity)
        for child in getattr(defender, "children", []) or [])
    await ctx.deal_damage(30 if evolved else 10)
    if evolved and ctx.attacker is not None:
        await ctx.deal_damage(10, target=ctx.attacker, apply_modifiers=False)

card = PokemonCardDef(
    guid="32470b60-ec5b-539e-b073-102b0b7b8d8a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrogue.Name",
    display_name="Tyrogue",
    searchable_by=["Tyrogue", "Basic", "Tyrogue"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=236,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Hitmonlee, Hitmonchan, or Hitmontop from your hand onto Tyrogue (this counts as evolving Tyrogue) and remove all damage counters from Tyrogue.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Gut Blow",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 10 damage plus 20 more damage and Tyrogue does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=_gut_blow,
        ),
    ],
)