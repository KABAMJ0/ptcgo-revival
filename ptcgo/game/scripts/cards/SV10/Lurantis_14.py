from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1e65ba4a-0c6f-5ff8-a18a-8037e559160b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1", "Lurantis"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Petal Blade Dance",
            game_text="Discard 2 Basic Grass Energy cards from your hand. If you can't discard 2 cards in this way, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)