from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c45f196e-008b-5f86-97a1-f22b6a23e0f5",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="DP4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Attack(
            title="Reach Over",
            game_text="Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Pursuit",
            game_text="If the Defending Pok\u00e9mon is Cresselia, this attack's base damage is 100.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=50,
            effect=unimplemented,
        ),
    ],
)