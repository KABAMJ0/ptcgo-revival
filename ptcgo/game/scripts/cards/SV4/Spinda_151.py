from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="22d0dd0e-c9e6-5561-b391-003fbdd77b58",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Ability(
            title="Tangled Feet",
            game_text="If this Pok\u00e9mon is Confused and is damaged by an attack, flip a coin. If heads, prevent that damage.",
            effect=unimplemented,
        ),
        Attack(
            title="Teetering Steps",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=condition_attack(SpecialConditions.CONFUSED, self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)