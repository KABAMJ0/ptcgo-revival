from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5d554146-df86-5294-8b08-ec551d021e48",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kricketot.Name",
    display_name="Kricketot",
    searchable_by=["Kricketot", "Basic", "Kricketot"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=401,
    abilities=[
        Attack(
            title="Lullaby",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)