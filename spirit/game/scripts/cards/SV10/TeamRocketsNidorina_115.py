from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b77f5e3e-20b9-5187-86ba-ccaca7125a9e",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorina.Name",
    display_name="Team Rocket's Nidorina",
    searchable_by=["Team Rocket's Nidorina", "Stage 1", "TeamRocketsNidorina"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoran.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Dark Awakening",
            game_text="Choose up to 2 of your Darkness Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a card that evolves from that Pok\u00e9mon and put it onto that Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
        ),
    ],
)