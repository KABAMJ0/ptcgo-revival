from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import Triggers


async def earthen_awakening(ctx):
    """Heal 20 from this Pokemon when an Energy card is attached to it."""
    attached = getattr(ctx, "attached_energy", None)
    if attached is None or ctx.energy_receiver is not ctx.source:
        return
    await ctx.heal(20, target=ctx.source)


card = PokemonCardDef(
    guid="69c1fa80-da82-5ed7-a73d-2bbe8abfc850",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Earthen Awakening",
            game_text="Whenever you attach an Energy card from your hand to this Pok\u00e9mon, heal 20 damage from it.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=earthen_awakening,
        ),
        Attack(
            title="Gigas Punch",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=flip_or_nothing(coins=2),
        ),
    ],
)