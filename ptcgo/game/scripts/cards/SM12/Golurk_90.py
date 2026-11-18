from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    count_discard,
    ignore_modifier_attack,
)


def _no_supporter_in_discard(ctx) -> bool:
    return count_discard("mine", _is_supporter)(ctx) == 0


def _is_supporter(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value

card = PokemonCardDef(
    guid="18ca5fa0-d9c5-51e3-b369-007cef785248",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
        Attack(
            title="Fist of Antiquity",
            game_text="If you have any Supporter cards in your discard pile, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=bonus_if(_no_supporter_in_discard, 0, else_nothing=True),
        ),
    ],
)