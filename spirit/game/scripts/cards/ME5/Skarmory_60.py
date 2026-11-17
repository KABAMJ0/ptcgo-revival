from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77ef3b05-3892-5028-b1d6-e6ec7d187753",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Steel Cutter",
            game_text="Discard up to 2 Basic Metal Energy cards from your hand, and this attack does 40 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)