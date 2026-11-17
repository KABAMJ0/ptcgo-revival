from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="956d190f-5b25-5095-868f-f3399b59db27",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eeveeex.Name",
    display_name="Eevee ex",
    searchable_by=["Eevee ex", "Basic", "Tera", "ex", "Eeveeex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=167,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
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