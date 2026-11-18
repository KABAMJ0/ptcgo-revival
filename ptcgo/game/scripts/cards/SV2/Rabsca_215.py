from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee824d37-41f6-5f4e-8dab-5a24ec3c134f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca", "Stage 1", "Rabsca"],
    subtypes=["Stage 1"],
    collector_number=215,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rellor.Name",
    family_id=953,
    abilities=[
        Attack(
            title="Revival Blessing",
            game_text="Put a Pok\u00e9mon from your discard pile onto your Bench.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)