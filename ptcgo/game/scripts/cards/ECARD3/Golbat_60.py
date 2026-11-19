from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="ab117a9d-8044-5753-83a9-711b8aa61897",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    display_name="Golbat",
    searchable_by=["Golbat", "Stage 1", "Golbat"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Poison Sound Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True, tails_conditions=(SpecialConditions.POISONED,)),
        ),
        Attack(
            title="Strength in Numbers",
            game_text="This attack does 30 damage plus 10 more damage for each Zubat, Golbat, and Crobat on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)