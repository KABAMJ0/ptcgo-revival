from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3bb1fbc0-61cb-507c-a43c-16ac859052bc",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Heavy Metal",
            game_text="Flip a coin for each Metal Energy attached to Lairon. This attack does 10 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Granite Head",
            game_text="During your opponent's next turn, any damage done to Lairon by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)