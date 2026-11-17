from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fdaca5d0-bc3c-5312-bac2-ddafa86a0f00",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    display_name="Carkol",
    searchable_by=["Carkol", "Stage 1", "Carkol"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Boulder Crush",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)