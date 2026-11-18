from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81e3fe26-5ed8-5733-bb0e-d63bc5c1f52b",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    display_name="Ekans",
    searchable_by=["Ekans", "Basic", "Ekans"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=23,
    abilities=[
        Attack(
            title="Poison Blend",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)