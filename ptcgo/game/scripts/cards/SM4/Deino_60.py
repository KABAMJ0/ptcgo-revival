from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be270b68-1243-5ac1-8e45-bc1f09edcb80",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    display_name="Deino",
    searchable_by=["Deino", "Basic", "Deino"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=633,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)