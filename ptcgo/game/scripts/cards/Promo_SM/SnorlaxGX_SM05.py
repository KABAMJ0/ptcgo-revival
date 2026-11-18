from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    AttrID,
    CLIENT_SPECIAL_CONDITION_NAMES,
    PokemonTypes,
    PokemonStage,
    Rarities,
    SpecialConditions,
)
from ptcgo.game.card_effects.attacks_common import bonus_if, condition_attack


def _is_asleep(ctx) -> bool:
    attacker = ctx.attacker
    return (attacker is not None
            and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
            in (attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))

card = PokemonCardDef(
    guid="284585c5-ca7c-5de6-9720-26d4cd90b869",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxGX.Name",
    display_name="Snorlax-GX",
    searchable_by=["Snorlax-GX", "Basic", "GX", "SnorlaxGX"],
    subtypes=["Basic", "GX"],
    collector_number=5,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Collapse",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
        Attack(
            title="Thunderous Snore",
            game_text="This attack can be used if this Pok\u00e9mon is Asleep. If it is not Asleep, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=180,
            effect=bonus_if(_is_asleep, 0, else_nothing=True),
            usable_despite_conditions=True,
        ),
        Attack(
            title="Pulverizing Pancake-GX",
            game_text="This Pok\u00e9mon is now Asleep. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 5},
            damage=210,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)