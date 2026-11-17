from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3dc60c6-ef8f-5d27-a053-94da53e1f73c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eeveeex.Name",
    display_name="Eevee ex",
    searchable_by=["Eevee ex", "Basic", "Tera", "ex", "Eeveeex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=174,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Rainbow DNA",
            game_text="This Pok\u00e9mon can evolve into any Pok\u00e9mon ex that evolves from Eevee if you play it from your hand onto this Pok\u00e9mon. (This Pok\u00e9mon can't evolve during your first turn or the turn you play it.)",
            effect=unimplemented,
        ),
        Attack(
            title="Coruscating Quartz",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
        ),
    ],
)