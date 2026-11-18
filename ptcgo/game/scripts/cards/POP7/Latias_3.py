from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="959d8721-8a10-5585-8bec-38775d6470de",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="POP7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=380,
    abilities=[
        Attack(
            title="Miraculous Light",
            game_text="Remove 2 damage counters and all Special Conditions from Latias.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Mist Ball",
            game_text="Discard a Fire and a Water Energy attached to Latias.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)