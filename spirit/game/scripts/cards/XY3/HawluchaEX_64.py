from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="118c19a7-bb73-5598-8f15-b732a9510c1d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HawluchaEX.Name",
    display_name="Hawlucha-EX",
    searchable_by=["Hawlucha-EX", "Basic", "EX", "HawluchaEX"],
    subtypes=["Basic", "EX"],
    collector_number=64,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=701,
    abilities=[
        Ability(
            title="Counterattack",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 2 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Moonsault Stomp",
            game_text="If there is any Stadium card in play, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)