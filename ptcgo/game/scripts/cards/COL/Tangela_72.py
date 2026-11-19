from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="c945ce8e-3765-525c-8d02-78b3e0b1de33",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic", "Tangela"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="COL",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=114,
    abilities=[
        Attack(
            title="Nutritional Support",
            game_text="Search your deck for a Grass Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)