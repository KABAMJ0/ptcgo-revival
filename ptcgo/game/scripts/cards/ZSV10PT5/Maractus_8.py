from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a17e4377-5be5-58e4-abbf-739883f9b664",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Attack(
            title="Lively Needles",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)