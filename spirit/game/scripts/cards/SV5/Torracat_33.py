from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ef155bc-3c30-5af6-81ea-e88bf3237048",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    display_name="Torracat",
    searchable_by=["Torracat", "Stage 1", "Torracat"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Flare Strike",
            game_text="During your next turn, this Pok\u00e9mon can't use Flare Strike.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)