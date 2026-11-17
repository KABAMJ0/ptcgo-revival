from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9e869a1c-798c-5e9b-9f24-bb296b7776f4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogi.Name",
    display_name="Okidogi",
    searchable_by=["Okidogi", "Basic", "Okidogi"],
    subtypes=["Basic"],
    collector_number=122,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Settle the Score",
            game_text="This attack does 60 more damage for each Prize card your opponent took during their last turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)