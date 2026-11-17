from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="24fc1c63-e217-5aa0-8ac2-9585a1f3c751",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Attack(
            title="Crystal Fall",
            game_text="If you have at least 4 Water Energy in play, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)