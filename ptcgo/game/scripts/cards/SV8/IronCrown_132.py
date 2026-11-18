from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f60779bf-7f1e-52b4-9ff5-f2394bd6c1ba",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronCrown.Name",
    display_name="Iron Crown",
    searchable_by=["Iron Crown", "Basic", "Future", "IronCrown"],
    subtypes=["Basic", "Future"],
    collector_number=132,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=1023,
    abilities=[
        Attack(
            title="Deleting Slash",
            game_text="If your opponent has 3 or more Benched Pok\u00e9mon, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)