from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2bb4f7f7-a2c8-56fb-be59-d8425e6eafa5",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Underwater Dive",
            game_text="Flip 2 coins. For each heads, remove 3 damage counters from Wailord.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Wailord. If the Defending Pok\u00e9mon has fewer remaining HP than Wailord, this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)