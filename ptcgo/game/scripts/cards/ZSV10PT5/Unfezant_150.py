from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dfdf2082-48ae-55de-acb3-964141e9e9e1",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Add On",
            game_text="Draw 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Swift Flight",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)