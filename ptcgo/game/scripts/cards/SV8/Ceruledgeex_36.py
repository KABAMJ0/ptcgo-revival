from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5dcb95c0-7902-53b0-9139-aec71f83908c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledgeex.Name",
    display_name="Ceruledge ex",
    searchable_by=["Ceruledge ex", "Stage 1", "Tera", "ex", "Ceruledgeex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=36,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Abyssal Flames",
            game_text="This attack does 20 more damage for each Energy card in your discard pile.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Raging Amethyst",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.METAL: 1},
            damage=280,
            effect=unimplemented,
        ),
    ],
)