from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="87923f87-a14e-5168-8513-c3658f1a214d",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsSnorlaxex.Name",
    display_name="Rocket's Snorlax ex",
    searchable_by=["Rocket's Snorlax ex", "Basic", "ex", "RocketsSnorlaxex"],
    subtypes=["Basic", "ex"],
    collector_number=104,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Dark Healer",
            game_text="As long as Rocket's Snorlax ex has any Darkness Energy attached to it, remove 1 damage counter from Rocket's Snorlax ex between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Collapse",
            game_text="Rocket's Snorlax ex is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=unimplemented,
        ),
    ],
)