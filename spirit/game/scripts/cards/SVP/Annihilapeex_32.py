from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="095e094a-ac62-577f-bfb9-148e7cc7ec82",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Annihilapeex.Name",
    display_name="Annihilape ex",
    searchable_by=["Annihilape ex", "Stage 2", "ex", "Annihilapeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=32,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=320,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name",
    family_id=979,
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