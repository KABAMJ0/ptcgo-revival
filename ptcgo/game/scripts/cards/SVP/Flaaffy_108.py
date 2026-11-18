from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="976d252a-fb74-5fd8-b219-cddc3e8cf5e1",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)