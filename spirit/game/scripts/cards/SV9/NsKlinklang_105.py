from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d8256795-2a21-5bd3-81bf-41cf707b9a6b",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlinklang.Name",
    display_name="N's Klinklang",
    searchable_by=["N's Klinklang", "Stage 2", "NsKlinklang"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlang.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Magnetic Blast",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 120 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)