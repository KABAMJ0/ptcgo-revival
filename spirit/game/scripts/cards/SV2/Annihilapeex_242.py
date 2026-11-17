from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7066eacc-16fe-5fc8-addd-dbfa61cce795",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilapeex.Name",
    display_name="Annihilape ex",
    searchable_by=["Annihilape ex", "Stage 2", "ex", "Annihilapeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=242,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=56,
    abilities=[
        Attack(
            title="Angry Grudge",
            game_text="Put up to 12 damage counters on this Pok\u00e9mon. This attack does 20 damage for each damage counter you placed in this way.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Seismic Toss",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)