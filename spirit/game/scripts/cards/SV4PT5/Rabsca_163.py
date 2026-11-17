from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="02d11693-47e3-55a9-882d-775ab48113d5",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rabsca.Name",
    display_name="Rabsca",
    searchable_by=["Rabsca", "Stage 1", "Rabsca"],
    subtypes=["Stage 1"],
    collector_number=163,
    set_code="SV4PT5",
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