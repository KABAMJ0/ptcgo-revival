from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="00ddee41-3038-580e-a46d-e1489578274d",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Bad Sleeping Habits",
            game_text="As long as Snorlax is Asleep, your opponent's Active Pok\u00e9mon can't retreat.",
            effect=unimplemented,
        ),
        Attack(
            title="Toss and Turn",
            game_text="If Snorlax is Asleep, this attack does 20 damage plus 30 more damage. (This attack can be used even if Snorlax is Asleep.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Press",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 40 more damage. If tails, Snorlax is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)