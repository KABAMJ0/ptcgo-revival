from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_prizes_remaining


def _six_prizes_left(ctx):
    return count_prizes_remaining("opponent")(ctx) == 6

card = PokemonCardDef(
    guid="724a17a3-cc91-56ea-9887-e40b728edac6",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kartana.Name",
    display_name="Kartana",
    searchable_by=["Kartana", "Basic", "Ultra Beast", "Kartana"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=101,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=798,
    abilities=[
        Attack(
            title="Divine Paper",
            game_text="If your opponent has exactly 6 Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(_six_prizes_left, 90),
        ),
    ],
)