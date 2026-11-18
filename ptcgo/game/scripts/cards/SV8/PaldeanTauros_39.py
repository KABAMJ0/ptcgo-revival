from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0dcb5a12-bab8-5cd1-b935-664f6ee68056",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic", "PaldeanTauros"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=128,
    abilities=[
        Attack(
            title="Upthrusting Horns",
            game_text="You may put 2 Energy attached to your opponent's Active Stage 2 Pok\u00e9mon into their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)