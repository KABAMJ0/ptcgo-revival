from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9477c8b9-b5ad-57d7-8982-81cf3d0f8c1f",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea δ",
    searchable_by=["Horsea \u03b4", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reverse Thrust",
            game_text="Switch Horsea with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)