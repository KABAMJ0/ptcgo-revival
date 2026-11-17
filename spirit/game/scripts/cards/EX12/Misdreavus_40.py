from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="958be97e-0208-5fae-8bc6-18fd80686e5d",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    display_name="Misdreavus",
    searchable_by=["Misdreavus", "Basic", "Misdreavus"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=200,
    abilities=[
        Ability(
            title="Deep Sleep",
            game_text="As long as Misdreavus is your Active Pok\u00e9mon, each player flips 2 coins for his or her Pok\u00e9mon that is Asleep between turns. If either coin is tails, that Pok\u00e9mon is still Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Return Trance",
            game_text="Return an Energy card attached to Misdreavus to your hand. The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dream Eater",
            game_text="If the Defending Pok\u00e9mon is not Asleep, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)