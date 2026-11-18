from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="571755a0-8055-5fec-824c-8053397a00a1",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    display_name="Floette",
    searchable_by=["Floette", "Stage 1", "Floette"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    family_id=669,
    abilities=[
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 30 more damage, and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)