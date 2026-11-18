from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bcb2a6b5-7430-599c-ae3d-7373d733a8bf",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name",
    display_name="Xerneas",
    searchable_by=["Xerneas", "Basic", "Xerneas"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=716,
    abilities=[
        Attack(
            title="Geo Storm",
            game_text="This attack does 30 damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)