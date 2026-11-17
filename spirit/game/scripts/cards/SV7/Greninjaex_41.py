from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1ed7f7cd-9409-58cd-b732-0013c84d599b",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex", "Greninjaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=41,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Attack(
            title="Shifting Shuriken",
            game_text="Flip a coin. If heads, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)