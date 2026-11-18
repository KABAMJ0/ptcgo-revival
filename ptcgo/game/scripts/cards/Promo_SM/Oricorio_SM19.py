from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    count_discard,
    place_counters,
    stadium_in_play_cond,
)


def _is_pokemon_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.POKEMON.value


def _no_stadium_in_play(ctx) -> bool:
    return not stadium_in_play_cond(ctx)

card = PokemonCardDef(
    guid="b8116976-2525-520e-b7bf-474367115a21",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorio.Name",
    display_name="Oricorio",
    searchable_by=["Oricorio", "Basic", "Oricorio"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=741,
    abilities=[
        Attack(
            title="Supernatural Dance",
            game_text="For each Pok\u00e9mon in your opponent's discard pile, put 1 damage counter on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(count_discard("opponent", _is_pokemon_card),
                          "choose_any_opponent"),
        ),
        Attack(
            title="Revelation Dance",
            game_text="If there is no Stadium card in play, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=bonus_if(_no_stadium_in_play, 0, else_nothing=True),
        ),
    ],
)