from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8cb95d1-ab44-57c6-93a3-a966fc230e8d",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKoffing.Name",
    display_name="Team Rocket's Koffing",
    searchable_by=["Team Rocket's Koffing", "Basic", "TeamRocketsKoffing"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=109,
    abilities=[
        Ability(
            title="Smog Signals",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), search your deck for up to 2 Pok\u00e9mon that have \"Koffing\" in their name and put them onto your Bench. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Leaking Gas",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)