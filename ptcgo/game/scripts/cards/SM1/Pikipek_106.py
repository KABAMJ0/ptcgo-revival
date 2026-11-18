from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3d352e4-7f64-5267-81fa-d01c53157afb",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    display_name="Pikipek",
    searchable_by=["Pikipek", "Basic", "Pikipek"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=731,
    abilities=[
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)