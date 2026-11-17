from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92e36fc2-8174-509c-9590-64e4ac0e14c7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFroslassex.Name",
    display_name="Mega Froslass ex",
    searchable_by=["Mega Froslass ex", "Stage 1", "MEGA", "ex", "MegaFroslassex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=47,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Resentful Refrain",
            game_text="This attack does 50 damage for each card in your opponent's hand.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Absolute Snow",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)