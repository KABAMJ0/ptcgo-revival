from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35944af1-e430-5830-91b9-0032529a6193",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    display_name="Duskull",
    searchable_by=["Duskull", "Basic", "Duskull"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=355,
    abilities=[
        Attack(
            title="Counting Song",
            game_text="Put up to 3 damage counters on Duskull. Then, put that many damage counters on the Defending Pok\u00e9mon.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Night Bind",
            game_text="Flip a coin. If heads, your opponent can't attach any Energy cards from his or her hand to the Active Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)