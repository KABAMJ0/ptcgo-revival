from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="69bac970-626e-57d2-86bf-419226d05927",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title="Burn It All Up",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)