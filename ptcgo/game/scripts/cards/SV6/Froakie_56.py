from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="202fb384-b905-5b36-b1f6-1d186fe5d16f",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic", "Froakie"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=656,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Froakie and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)