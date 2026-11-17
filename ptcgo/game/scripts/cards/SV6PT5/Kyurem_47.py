from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9286fd09-1515-5602-8b39-1657e9119acf",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=646,
    abilities=[
        Ability(
            title="Plasma Bane",
            game_text="If your opponent has any cards in their discard pile that have \"Colress\" in the name, this Pok\u00e9mon can use the Trifrost attack for Colorless.",
            effect=unimplemented,
        ),
        Attack(
            title="Trifrost",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 110 damage to 3 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)