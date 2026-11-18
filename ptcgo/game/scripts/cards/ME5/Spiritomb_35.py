from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c675dd7-c3f0-5e58-8cba-e84a22acec13",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=442,
    abilities=[
        Attack(
            title="Spiritual End",
            game_text="If you have 13 or more Pok\u00e9mon that have the Hide 'n' Sneak Ability in your discard pile, choose 2 of your opponent's Pok\u00e9mon and quadruple the number of damage counters on each of them.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)