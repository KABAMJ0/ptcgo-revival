from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54290782-4692-521b-9dbb-7098fbf1c44b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMewtwoex.Name",
    display_name="Team Rocket's Mewtwo ex",
    searchable_by=["Team Rocket's Mewtwo ex", "Basic", "ex", "TeamRocketsMewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=213,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="This Pok\u00e9mon can't attack unless you have 4 or more Team Rocket's Pok\u00e9mon in play.",
            effect=unimplemented,
        ),
        Attack(
            title="Erasure Ball",
            game_text="You may discard up to 2 Energy from your Benched Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)