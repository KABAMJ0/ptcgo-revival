from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="306ab48e-6271-5f36-9b9d-c1da14318776",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic", "Finizen"],
    subtypes=["Basic"],
    collector_number=21,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    abilities=[
        Attack(
            title="Draining Fin",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=unimplemented,
        ),
    ],
)