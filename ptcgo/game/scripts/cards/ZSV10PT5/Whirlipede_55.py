from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b0b5137e-452d-5287-8345-95ddef54fbac",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name",
    display_name="Whirlipede",
    searchable_by=["Whirlipede", "Stage 1", "Whirlipede"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name",
    family_id=543,
    abilities=[
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)