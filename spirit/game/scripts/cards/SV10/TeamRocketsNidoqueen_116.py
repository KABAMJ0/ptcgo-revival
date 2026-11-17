from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="516c7e41-8883-5d5a-8cca-9281b4d34afe",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoqueen.Name",
    display_name="Team Rocket's Nidoqueen",
    searchable_by=["Team Rocket's Nidoqueen", "Stage 2", "TeamRocketsNidoqueen"],
    subtypes=["Stage 2"],
    collector_number=116,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Love Impact",
            game_text="If a Pok\u00e9mon that has \"Nidoking\" in its name is on your Bench, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Mega Kick",
            cost={PokemonTypes.DARKNESS: 2},
            damage=130,
        ),
    ],
)