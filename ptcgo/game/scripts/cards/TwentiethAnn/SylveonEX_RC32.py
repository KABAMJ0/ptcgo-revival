from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.attributes import AttrID


def _fairy_energy(card):
    return energy_provides_type(card, PokemonTypes.FAIRY.value)


async def _heal_receiver(ctx, moved):
    for _card, holder in moved:
        missing = ctx.max_hp(holder) - holder.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(min(50, missing), holder)


async def precious_ribbon(ctx):
    """Printed 100, move a Fairy Energy from this Pokemon to 1 of your Benched
    Pokemon, healing 50 from that Pokemon if you did."""
    await ctx.deal_damage()
    await move_energy_between(
        predicate=_fairy_energy, count=1, from_pool="active", to_pool="bench",
        then=_heal_receiver,
    )(ctx)

card = PokemonCardDef(
    guid="cc1855e8-e31d-5c84-842e-95ecaf9d5a08",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonEX.Name",
    display_name="Sylveon-EX",
    searchable_by=["Sylveon-EX", "Basic", "EX", "SylveonEX"],
    subtypes=["Basic", "EX"],
    collector_number=10032,
    set_code="TwentiethAnn",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=700,
    abilities=[
        Attack(
            title="Dress Up",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=mill_attack(1, opponent=True),
        ),
        Attack(
            title="Precious Ribbon",
            game_text="Move a Fairy Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. If you do, heal 50 damage from that Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=precious_ribbon,
        ),
    ],
)