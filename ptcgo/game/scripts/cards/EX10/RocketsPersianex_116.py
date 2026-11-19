from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9371de7d-4e2c-5269-8fef-9b18997ddab6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsPersianex.Name",
    display_name="Rocket's Persian ex",
    searchable_by=["Rocket's Persian ex", "Stage 1", "ex", "RocketsPersianex"],
    subtypes=["Stage 1", "ex"],
    collector_number=116,
    set_code="EX10",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsMeowth.Name",
    family_id=53,
    abilities=[
        Ability(
            title="Night Cry",
            game_text="Once during your turn, if Rocket's Persian ex is on your Bench, you may search your deck for a Pok\u00e9mon with Dark or Rocket's in its name. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            effect=unimplemented,
        ),
        Attack(
            title="Toxic Claws",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Put 2 damage counters instead of 1 on the Defending Pok\u00e9mon between turns.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=unimplemented,
        ),
    ],
)