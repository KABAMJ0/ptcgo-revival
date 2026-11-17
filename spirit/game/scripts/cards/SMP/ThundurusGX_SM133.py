from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2c8f9ca4-0c36-5ddb-bfa2-48a06209792c",
    key="SMP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusGX.Name",
    display_name="Thundurus-GX",
    searchable_by=["Thundurus-GX", "Basic", "GX", "ThundurusGX"],
    subtypes=["Basic", "GX"],
    collector_number=133,
    set_code="SMP",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=642,
    abilities=[
        Attack(
            title="Charge",
            game_text="Search your deck for a Lightning Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Electric Ball",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=140,
        ),
        Attack(
            title="Thundering Hurricane-GX",
            game_text="Flip 4 coins. This attack does 100 damage for each heads. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)