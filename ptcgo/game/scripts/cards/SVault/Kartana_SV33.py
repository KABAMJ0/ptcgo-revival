from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee10c83a-5f4a-50c0-a8a6-b7ea63146a0a",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kartana.Name",
    display_name="Kartana",
    searchable_by=["Kartana", "Basic", "Ultra Beast", "Kartana"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=33,
    set_code="SVault",
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
            effect=unimplemented,
        ),
    ],
)