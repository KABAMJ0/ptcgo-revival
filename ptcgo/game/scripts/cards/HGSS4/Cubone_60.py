from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3d677e96-ce6c-5ad4-9642-a74f61f25dbb",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=104,
    abilities=[
        Ability(
            title="Lonely Bone",
            game_text="Any damage done to Cubone by your opponent's attacks is reduced by 20 for each Marowak in your discard pile (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Bone Rush",
            game_text="Flip a coin until you get tails. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
    ],
)