from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="897fb324-a15c-5d8a-91b1-c8489e4ccadf",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=605,
    abilities=[
        Attack(
            title="Slight Shift",
            game_text="Move an Energy from 1 of your opponent's Pok\u00e9mon to another of their Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)