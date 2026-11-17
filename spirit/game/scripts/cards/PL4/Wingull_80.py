from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="011d2459-c4dd-5ea0-9357-986e3e10be79",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    display_name="Wingull",
    searchable_by=["Wingull", "Basic", "Wingull"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=278,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Slashing Strike",
            game_text="During your next turn, Wingull can't use Slashing Strike.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)