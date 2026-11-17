from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="88a68e3c-ed0f-5071-9934-8ede055f20bd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Eiscue"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Frigid Block",
            game_text="Discard all Energy from this Pok\u00e9mon. During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)