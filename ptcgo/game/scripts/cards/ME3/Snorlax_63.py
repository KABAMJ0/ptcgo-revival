from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="1ee374af-2730-52bb-a786-05ec77d0df96",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Gormandizer",
            game_text="Flip a coin until you get tails. Search your deck for an amount of Basic Energy up to the number of heads and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Collapse",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=160,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)