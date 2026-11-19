from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="edba2910-1eaf-5532-ba51-2a3e78bdd64b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pecharunt.Name",
    display_name="Pecharunt",
    searchable_by=["Pecharunt", "Basic", "Pecharunt"],
    subtypes=["Basic"],
    collector_number=149,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1025,
    abilities=[
        Ability(
            title="Toxic Subjugation",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, put 5 more damage counters on your opponent's Poisoned Pok\u00e9mon during Pok\u00e9mon Checkup.",
            effect=unimplemented,
        ),
        Attack(
            title="Poison Chain",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
    ],
)