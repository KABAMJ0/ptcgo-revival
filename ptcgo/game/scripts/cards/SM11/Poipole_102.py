from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_prizes_remaining


def _both_down_to_one(ctx):
    return (count_prizes_remaining("mine")(ctx) == 1
            and count_prizes_remaining("opponent")(ctx) == 1)

card = PokemonCardDef(
    guid="6fde8418-5e7e-5616-baa5-f27bdf2f2e25",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    display_name="Poipole",
    searchable_by=["Poipole", "Basic", "Ultra Beast", "Poipole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=102,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=803,
    abilities=[
        Attack(
            title="Belt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Last Scene",
            game_text="If each player has exactly 1 Prize card remaining, this attack does 130 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_both_down_to_one, 130),
        ),
    ],
)