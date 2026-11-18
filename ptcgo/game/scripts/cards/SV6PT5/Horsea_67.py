from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6185c79-b0aa-5f5d-ba5b-eca61a0aac89",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SV6PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)