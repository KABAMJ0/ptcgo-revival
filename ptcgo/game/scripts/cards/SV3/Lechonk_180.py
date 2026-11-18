from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="457ddde3-0d0f-5b52-9e92-89c60cab7f32",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    display_name="Lechonk",
    searchable_by=["Lechonk", "Basic", "Lechonk"],
    subtypes=["Basic"],
    collector_number=180,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=915,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)