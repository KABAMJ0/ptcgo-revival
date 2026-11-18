from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ebcc823-d128-5d0a-99b7-58f043411970",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golurk.Name",
    display_name="Golurk",
    searchable_by=["Golurk", "Stage 1", "Golurk"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    family_id=622,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fighting Fist",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex or Pok\u00e9mon V, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)