from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import condition_attack


async def sky_hurricane(ctx):
    """Printed damage, then this attack is locked through the user's next turn."""
    await ctx.deal_damage()
    ability = ctx.ability
    if ctx.attacker is not None and ability is not None and ability.ability_id:
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id,
                                          ability.ability_id)

card = PokemonCardDef(
    guid="8a9083b2-4dc6-5495-80f1-6fecde736c4f",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CorviknightV.Name",
    display_name="Corviknight V",
    searchable_by=["Corviknight V", "Basic", "V", "CorviknightV"],
    subtypes=["Basic", "V"],
    collector_number=18,
    set_code="SWSH12TG",
    rarity=Rarities.RareHoloV,
    hp=210,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=823,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
        Attack(
            title="Sky Hurricane",
            game_text="During your next turn, this Pok\u00e9mon can't use Sky Hurricane.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            locks_next_turn=True,
            effect=sky_hurricane,
        ),
    ],
)