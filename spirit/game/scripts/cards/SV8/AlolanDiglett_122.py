from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3675f578-d0ae-5fef-ad74-52c15bad8a11",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic", "AlolanDiglett"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=30,
            effect=unimplemented,
        ),
    ],
)