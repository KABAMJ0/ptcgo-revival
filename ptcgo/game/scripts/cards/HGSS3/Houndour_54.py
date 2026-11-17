from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b4c3fd15-ee54-5dab-ab59-bbf064b6c8c0",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=228,
    abilities=[
        Attack(
            title="Jump On",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)