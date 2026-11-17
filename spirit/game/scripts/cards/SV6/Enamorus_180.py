from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ca471d9-030d-5bc3-9ad6-5191915770bb",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Enamorus.Name",
    display_name="Enamorus",
    searchable_by=["Enamorus", "Basic", "Enamorus"],
    subtypes=["Basic"],
    collector_number=180,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=905,
    abilities=[
        Attack(
            title="Heart Sign",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Love Resonance",
            game_text="If any of your Pok\u00e9mon in play are the same type as any of your opponent's Pok\u00e9mon in play, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)