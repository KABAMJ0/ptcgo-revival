from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f6c12733-1bce-5046-96ed-d00d8a6b5084",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    display_name="Misty's Psyduck",
    searchable_by=["Misty's Psyduck", "Basic", "MistysPsyduck"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Ability(
            title="Flustered Leap",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may discard the bottom card of your deck. If you do, discard all cards from this Pok\u00e9mon and put this Pok\u00e9mon on top of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Sprinkle Water",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)