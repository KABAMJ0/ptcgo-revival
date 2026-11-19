from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c302a94-91a2-5852-9b90-f68a3f36512a",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    display_name="Litwick",
    searchable_by=["Litwick", "Basic", "Litwick"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=607,
    abilities=[
        Attack(
            title="Firebreathing",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)