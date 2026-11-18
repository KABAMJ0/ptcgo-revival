from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ef19d713-b5c6-5cf5-8b2c-994b926b833b",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    display_name="Vullaby",
    searchable_by=["Vullaby", "Basic", "Vullaby"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
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