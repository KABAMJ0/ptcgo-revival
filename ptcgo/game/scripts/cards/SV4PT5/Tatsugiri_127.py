from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="852db530-7c7c-5c3a-97a3-568ee8db19ec",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic", "Tatsugiri"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=978,
    abilities=[
        Attack(
            title="Mise en Place",
            game_text="Search your deck for up to 2 Basic Water Energy cards and attach them to 1 of your Basic Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Curl Up",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)