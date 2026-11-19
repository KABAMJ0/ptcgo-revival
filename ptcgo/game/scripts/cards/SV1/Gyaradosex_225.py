from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="af72f278-fd4e-5c27-88c6-1d3cb8395de7",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyaradosex.Name",
    display_name="Gyarados ex",
    searchable_by=["Gyarados ex", "Stage 1", "Tera", "ex", "Gyaradosex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=225,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
        Attack(
            title="Tyrannical Tail",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 180 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
            damage_operator="+",
            effect=bonus_if(has_damage(), 180),
        ),
    ],
)