from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ab515a4d-3fee-52a4-a481-8e3d8ce6ea64",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogi.Name",
    display_name="Okidogi",
    searchable_by=["Okidogi", "Basic", "Okidogi"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Adrena-Power",
            game_text="If this Pok\u00e9mon has any Darkness Energy attached, it gets +100 HP, and the attacks it uses do 100 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Good Punch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
        ),
    ],
)