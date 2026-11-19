from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, opponent_prizes_taken_at_least


card = PokemonCardDef(
    guid="c5e49d46-00af-5fb5-b047-fcaceea2f16f",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zacian.Name",
    display_name="Zacian",
    searchable_by=["Zacian", "Basic", "Zacian"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=888,
    abilities=[
        Attack(
            title="Limit Break",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bonus_if(opponent_prizes_taken_at_least(3), 90),
        ),
    ],
)