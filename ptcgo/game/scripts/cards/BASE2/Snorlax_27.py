from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

from ptcgo.game.card_effects.passives_common import condition_immunity_passive
from ptcgo.game.attributes import SpecialConditions

_thick_skinned = condition_immunity_passive([
    SpecialConditions.ASLEEP, SpecialConditions.CONFUSED,
    SpecialConditions.PARALYZED, SpecialConditions.POISONED,
])

card = PokemonCardDef(
    guid="b5a3e945-bc6c-5bda-b932-c42381f59246",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=143,
    abilities=[
        Ability(
            title="Thick Skinned",
            game_text="Snorlax can't become Asleep, Confused, Paralyzed, or Poisoned. This power can't be used if Snorlax is already Asleep, Confused, or Paralyzed.",
            passive=_thick_skinned,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)