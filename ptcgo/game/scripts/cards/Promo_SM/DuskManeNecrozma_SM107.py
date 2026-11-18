from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    count_prizes_remaining,
    snipe_attack,
)
from ptcgo.game.data_utils import subtypes_for


def _is_gx_or_ex(pokemon) -> bool:
    subtypes = subtypes_for(pokemon.archetype_id)
    return "GX" in subtypes or "EX" in subtypes


def _opponent_has_one_prize(ctx) -> bool:
    return count_prizes_remaining("opponent")(ctx) == 1

card = PokemonCardDef(
    guid="6fc7dbc3-c3f5-59fe-9f83-dd6686596065",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DuskManeNecrozma.Name",
    display_name="Dusk Mane Necrozma",
    searchable_by=["Dusk Mane Necrozma", "Basic", "Ultra Beast", "DuskManeNecrozma"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=107,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Attack(
            title="Dusk Shot",
            game_text="This attack does 60 damage to 1 of your opponent's Pok\u00e9mon-GX or Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.METAL: 1},
            effect=snipe_attack(60, pool=_is_gx_or_ex, count=1, apply_modifiers=False),
        ),
        Attack(
            title="Rusty Claws",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 100 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=bonus_if(_opponent_has_one_prize, 100),
        ),
    ],
)