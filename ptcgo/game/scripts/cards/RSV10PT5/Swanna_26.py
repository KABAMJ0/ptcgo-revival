from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28d6661d-9e77-5b53-9f8b-69ab19f034b1",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swanna.Name",
    display_name="Swanna",
    searchable_by=["Swanna", "Stage 1", "Swanna"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    family_id=580,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)