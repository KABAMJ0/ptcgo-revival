from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5bc46a50-cc40-5835-abaa-ec4d80b484a2",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=303,
    abilities=[
        Attack(
            title="Double Eater",
            game_text="Discard up to 2 Energy cards from your hand, and this attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)