from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c73fc42-6109-577b-9092-d44630a8f10b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarumaka.Name",
    display_name="N's Darumaka",
    searchable_by=["N's Darumaka", "Basic", "NsDarumaka"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)