from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ad6c3d7-b1a5-5978-b99a-bebff1a30506",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlutterMane.Name",
    display_name="Flutter Mane",
    searchable_by=["Flutter Mane", "Basic", "Ancient", "FlutterMane"],
    subtypes=["Basic", "Ancient"],
    collector_number=97,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=987,
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