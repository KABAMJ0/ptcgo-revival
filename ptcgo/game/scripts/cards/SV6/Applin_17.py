from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45fa460a-fa39-5294-be7c-62ba3d39cad4",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    display_name="Applin",
    searchable_by=["Applin", "Basic", "Applin"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=840,
    abilities=[
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)