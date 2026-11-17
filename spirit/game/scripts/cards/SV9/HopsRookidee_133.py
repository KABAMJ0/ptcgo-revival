from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3c968496-3622-5f92-b2a2-7784b7e57a06",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsRookidee.Name",
    display_name="Hop's Rookidee",
    searchable_by=["Hop's Rookidee", "Basic", "HopsRookidee"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=821,
    abilities=[
        Attack(
            title="Intimidating Stare",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)