from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="563f0480-b37d-52d7-9f1e-3628f2bf5dc4",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2", "Florges"],
    subtypes=["Stage 2"],
    collector_number=93,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Blooming Garden",
            game_text="Your Pok\u00e9mon in play have no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon's attacks do 30 less damage\u00a0(before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)