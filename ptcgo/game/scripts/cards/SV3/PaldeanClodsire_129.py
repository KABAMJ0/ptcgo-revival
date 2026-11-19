from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_condition, condition_attack
card = PokemonCardDef(
    guid="1fce15e9-669d-50ee-bf7d-9c51a35b1941",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name",
    display_name="Paldean Clodsire",
    searchable_by=["Paldean Clodsire", "Stage 1", "PaldeanClodsire"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pok\u00e9mon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, both_actives=True),
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(defender_has_condition(SpecialConditions.POISONED), 120),
        ),
    ],
)