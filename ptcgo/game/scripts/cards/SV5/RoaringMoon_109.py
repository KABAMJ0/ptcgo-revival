from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import count_discard, damage_per
from ptcgo.game.card_effects.trainers import pokemon_of_subtype
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="08649fb1-59e7-5069-8dbc-f9fa9d4baa6d",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RoaringMoon.Name",
    display_name="Roaring Moon",
    searchable_by=["Roaring Moon", "Basic", "Ancient", "RoaringMoon"],
    subtypes=["Basic", "Ancient"],
    collector_number=109,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1005,
    abilities=[
        Attack(
            title="Vengeance Fletching",
            game_text="This attack does 10 more damage for each Ancient card in your discard pile.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_discard("mine", pokemon_of_subtype("Ancient")), 10, base=70),
        ),
        Attack(
            title="Speed Wing",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)