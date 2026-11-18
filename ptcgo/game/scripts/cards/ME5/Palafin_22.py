from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edd7ee4e-7c35-59b5-af75-82db66830f7b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1", "Palafin"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Knuckle Justice",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)