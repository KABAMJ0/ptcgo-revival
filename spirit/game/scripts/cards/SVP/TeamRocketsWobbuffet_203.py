from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cfb21a6a-9a5c-5bc8-a8a0-ba2aa98685da",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsWobbuffet.Name",
    display_name="Team Rocket's Wobbuffet",
    searchable_by=["Team Rocket's Wobbuffet", "Basic", "TeamRocketsWobbuffet"],
    subtypes=["Basic"],
    collector_number=203,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=202,
    abilities=[
        Attack(
            title="Rocket Mirror",
            game_text="Move all damage counters from 1 of your Benched Team Rocket's Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)