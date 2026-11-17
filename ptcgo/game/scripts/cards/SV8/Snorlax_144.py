from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c8e15a1c-3f1e-529c-a49c-368c8572d4e3",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Mega Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)