from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16575380-dc2a-5ad4-a4d9-c5db0cc2c234",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic", "Starly"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=396,
    abilities=[
        Attack(
            title="Bug Search",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)