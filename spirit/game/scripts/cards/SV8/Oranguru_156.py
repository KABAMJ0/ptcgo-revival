from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="742e9847-def9-569a-9b9d-38e93c8c856e",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic", "Oranguru"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Attack(
            title="Now You're in My Power",
            game_text="Until the end of your next turn, the Defending Pok\u00e9mon's Weakness is now Colorless. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)