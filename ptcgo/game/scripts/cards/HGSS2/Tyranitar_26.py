from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa62cd15-2f1a-58ea-af75-57b0ffa32327",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Tail Crush",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)