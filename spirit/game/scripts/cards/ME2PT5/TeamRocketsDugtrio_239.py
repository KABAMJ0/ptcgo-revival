from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c13a4765-b810-5236-a31d-65617f8f03df",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDugtrio.Name",
    display_name="Team Rocket's Dugtrio",
    searchable_by=["Team Rocket's Dugtrio", "Stage 1", "TeamRocketsDugtrio"],
    subtypes=["Stage 1"],
    collector_number=239,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Holes",
            game_text="Whenever your opponent's Active Pok\u00e9mon moves to the Bench during their turn, place 2 damage counters on that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)