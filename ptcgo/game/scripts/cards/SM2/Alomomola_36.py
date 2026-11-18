from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40dde91f-4344-541d-9fa5-77f488ef5897",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alomomola.Name",
    display_name="Alomomola",
    searchable_by=["Alomomola", "Basic", "Alomomola"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=594,
    abilities=[
        Attack(
            title="Borne Ashore",
            game_text="Put a Basic Pok\u00e9mon from either player's discard pile onto its owner's Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)