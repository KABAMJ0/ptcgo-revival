from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2620f05-ea23-538c-82a8-01d198cddec6",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlutterMane.Name",
    display_name="Flutter Mane",
    searchable_by=["Flutter Mane", "Basic", "Ancient", "FlutterMane"],
    subtypes=["Basic", "Ancient"],
    collector_number=43,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Ability(
            title="Midnight Fluttering",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent's Active Pok\u00e9mon has no Abilities, except for Midnight Fluttering.",
            effect=unimplemented,
        ),
        Attack(
            title="Hex Hurl",
            game_text="Put 2 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=unimplemented,
        ),
    ],
)