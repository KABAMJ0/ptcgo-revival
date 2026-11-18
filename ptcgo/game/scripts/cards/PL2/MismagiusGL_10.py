from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="60518b08-a613-53bd-97de-8566a6e10abd",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MismagiusGL.Name",
    display_name="Mismagius GL",
    searchable_by=["Mismagius GL", "Basic", "SP", "MismagiusGL"],
    subtypes=["Basic", "SP"],
    collector_number=10,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=429,
    abilities=[
        Attack(
            title="Psychic Removal",
            game_text="Flip 2 coins. If both of them are heads, discard all Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Grudge",
            game_text="Does 20 damage plus 10 more damage for each Prize card your opponent has taken.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)