from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="4cf4ef15-abcc-5d79-b46d-5959c438028e",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name",
    display_name="Lickitung",
    searchable_by=["Lickitung", "Basic", "Lickitung"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=108,
    abilities=[
        Attack(
            title="Lick",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)