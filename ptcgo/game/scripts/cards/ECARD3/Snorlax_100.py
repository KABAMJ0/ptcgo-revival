from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import is_in_active_spot, unafflicted
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _lolling_ready(board, player_id, pokemon) -> bool:
    return (is_in_active_spot(pokemon) and unafflicted(board, player_id, pokemon)
            and pokemon.get_attribute(AttrID.HP, 0) < passives_ref(board, pokemon))


def passives_ref(board, pokemon):
    from ptcgo.game.session.passives import effective_max_hp
    return effective_max_hp(board, pokemon)


async def _lolling_about(ctx):
    await ctx.heal(10, ctx.attacker)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)

card = PokemonCardDef(
    guid="2651e3e0-6347-596d-9c2a-9cc1bbaed796",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Lolling About",
            game_text="Once during your turn (before your attack), if Snorlax is your Active Pok\u00e9mon, you may remove 1 damage counter from Snorlax. Snorlax is now Asleep. This power can't be used if Snorlax is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_lolling_ready,
            effect=_lolling_about,
        ),
        Attack(
            title="Continuous Tumble",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(per_heads=30, until_tails=True),
        ),
    ],
)
