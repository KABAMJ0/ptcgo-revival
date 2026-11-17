from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4c60dfe0-61ad-5179-9d26-f9f905113da0",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDragalgeex.Name",
    display_name="Mega Dragalge ex",
    searchable_by=["Mega Dragalge ex", "Stage 1", "MEGA", "ex", "MegaDragalgeex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=104,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    family_id=690,
    abilities=[
        Attack(
            title="Corrosive Liquid",
            game_text="Discard all Pok\u00e9mon Tools and Special Energy from all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Pernicious Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. During Pok\u00e9mon Checkup, place 16 damage counters on that Pok\u00e9mon instead of 1.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)