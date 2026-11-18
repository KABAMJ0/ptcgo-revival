from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31f383d5-bec6-50f6-9f97-93ac462f0f73",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynxex.Name",
    display_name="Jynx ex",
    searchable_by=["Jynx ex", "Basic", "ex", "Jynxex"],
    subtypes=["Basic", "ex"],
    collector_number=191,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=124,
    abilities=[
        Attack(
            title="Heart-Stopping Kiss",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, it is Knocked Out.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)