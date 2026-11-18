from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1680c662-5b7d-5a34-baab-9d11fe204fd1",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=135,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=426,
    abilities=[
        Attack(
            title="Everyone Explode Now",
            game_text="This attack does 50 damage for each of your Drifloon and Drifblim in play. This attack also does 30 damage to each of your Drifloon and Drifblim. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)