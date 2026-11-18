from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc1b0b5c-7ca6-5837-ab0b-5df8151f1cd8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Inviting Scent",
            game_text="Switch in 1 of your opponent's Benched Pok\u00e9mon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)