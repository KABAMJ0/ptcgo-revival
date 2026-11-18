from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7440a2c-ae58-5880-84fa-1beb280560ec",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trumbeak.Name",
    display_name="Trumbeak",
    searchable_by=["Trumbeak", "Stage 1", "Trumbeak"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikipek.Name",
    family_id=731,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)