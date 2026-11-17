from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a0c95ded-3f24-523b-a730-9a7ddd8ddbc9",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic", "Durant"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=632,
    abilities=[
        Attack(
            title="Bite Together",
            game_text="If Durant is on your Bench, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)