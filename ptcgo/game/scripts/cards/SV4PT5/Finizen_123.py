from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b3b9c1a-5fa9-5bd1-a282-ee74773c1e19",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic", "Finizen"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Valiant Evolution",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)