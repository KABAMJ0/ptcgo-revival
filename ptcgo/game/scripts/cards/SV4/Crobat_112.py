from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c650a3c-a01a-5f5f-8eba-891b2bccb143",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    display_name="Crobat",
    searchable_by=["Crobat", "Stage 2", "Crobat"],
    subtypes=["Stage 2"],
    collector_number=112,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Attack(
            title="Echoing Madness",
            game_text="Choose Item cards or Supporter cards. During your opponent's next turn, they can't play any of the chosen cards from their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)