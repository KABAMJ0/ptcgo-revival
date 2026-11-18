from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4f8b2c0-f8ad-530a-b0cd-0a6a2ea4fb8a",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    display_name="Yamper",
    searchable_by=["Yamper", "Basic", "Yamper"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=835,
    abilities=[
        Attack(
            title="Whimsy Tackle",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)