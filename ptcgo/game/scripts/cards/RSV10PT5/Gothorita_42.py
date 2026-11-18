from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="48a80eb0-b542-5161-9257-1543d8a31e4b",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1", "Gothorita"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)