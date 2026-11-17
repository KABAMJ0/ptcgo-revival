from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9525dcfb-8cb9-586a-9023-c563faef90b6",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seismitoad.Name",
    display_name="Seismitoad",
    searchable_by=["Seismitoad", "Stage 2", "Seismitoad"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    family_id=535,
    abilities=[
        Ability(
            title="Quaking Zone",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, attacks used by your opponent's Active Pok\u00e9mon cost Colorless more.",
            effect=unimplemented,
        ),
        Attack(
            title="Echoed Voice",
            game_text="During your next turn, this Pok\u00e9mon's Echoed Voice attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)