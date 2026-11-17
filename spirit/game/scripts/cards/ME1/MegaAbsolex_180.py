from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dbffef9b-3fa5-5230-8169-8af2557e469c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAbsolex.Name",
    display_name="Mega Absol ex",
    searchable_by=["Mega Absol ex", "Basic", "MEGA", "ex", "MegaAbsolex"],
    subtypes=["Basic", "MEGA", "ex"],
    collector_number=180,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=359,
    abilities=[
        Attack(
            title="Terminal Period",
            game_text="If your opponent's Active Pok\u00e9mon has exactly 6 damage counters on it, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Claw of Darkness",
            game_text="Your opponent reveals their hand, and you discard a card you find there.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)