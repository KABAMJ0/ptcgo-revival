from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42edfe01-b0cd-51ee-bdf2-52c775ab44af",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabscaex.Name",
    display_name="Rabsca ex",
    searchable_by=["Rabsca ex", "Stage 1", "ex", "Rabscaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=25,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Upside-Down Draw",
            game_text="Draw 3 cards from the bottom of your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 90 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)