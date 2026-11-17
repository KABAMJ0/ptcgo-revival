from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fdf108d8-b320-5b8c-bf31-9460d5d24381",
    key="SMP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuFini.Name",
    display_name="Tapu Fini",
    searchable_by=["Tapu Fini", "Basic", "TapuFini"],
    subtypes=["Basic"],
    collector_number=203,
    set_code="SMP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=788,
    abilities=[
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Nature Wave",
            game_text="If your opponent has any Ultra Beasts in play, this attack can be used for Colorless.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)