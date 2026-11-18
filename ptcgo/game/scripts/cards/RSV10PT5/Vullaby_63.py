from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72166619-9f0f-5d56-81da-3c09d44d696d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic", "Vullaby"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=629,
    abilities=[
        Attack(
            title="Playful Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)