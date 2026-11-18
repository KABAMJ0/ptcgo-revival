from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="473081cb-fcb8-51d1-ac9b-f8e06b70bb9b",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic", "Hawlucha"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Attack(
            title="Prize Count",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)