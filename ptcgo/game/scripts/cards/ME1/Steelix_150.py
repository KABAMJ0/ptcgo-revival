from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a0b0ed7-41e6-56ca-b3e9-76a04ee0839e",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Steelix"],
    subtypes=["Stage 1"],
    collector_number=150,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Welcoming Tail",
            game_text="If you have exactly 6 Prize cards remaining, this attack does 200 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)