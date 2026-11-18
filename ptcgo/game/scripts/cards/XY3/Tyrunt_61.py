from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="029c0ade-d5c8-5115-b03a-638735bbb0df",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    display_name="Tyrunt",
    searchable_by=["Tyrunt", "Restored", "Tyrunt"],
    subtypes=["Restored"],
    collector_number=61,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.JawFossil.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)