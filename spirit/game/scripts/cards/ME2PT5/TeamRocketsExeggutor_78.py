from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6598f8a6-a946-5b73-b55c-bcf64fef42c1",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsExeggutor.Name",
    display_name="Team Rocket's Exeggutor",
    searchable_by=["Team Rocket's Exeggutor", "Stage 1", "TeamRocketsExeggutor"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsExeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tri Kinesis",
            game_text="Flip 3 coins. If all of them are heads, Knock Out 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Double-Edge",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)