from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aadc621b-74ed-5a3d-b3d5-45da9d5f4fc8",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dolliv.Name",
    display_name="Dolliv",
    searchable_by=["Dolliv", "Stage 1", "Dolliv"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Smoliv.Name",
    family_id=928,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Apply Oil",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)