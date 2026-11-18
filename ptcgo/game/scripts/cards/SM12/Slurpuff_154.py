from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    condition_attack,
    defender_has_condition,
)

card = PokemonCardDef(
    guid="c5fd3e8e-64a6-5483-a756-2924be50abf7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="SM12",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Attack(
            title="Olfactory Enchantment",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 1},
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Sweet Panic",
            game_text="If your opponent's Active Pok\u00e9mon isn't Confused, this attack does nothing.",
            cost={PokemonTypes.FAIRY: 1},
            damage=110,
            effect=bonus_if(defender_has_condition(SpecialConditions.CONFUSED), 0,
                      else_nothing=True),
        ),
    ],
)