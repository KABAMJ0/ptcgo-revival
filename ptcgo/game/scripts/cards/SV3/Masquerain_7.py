from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee3a3b34-5072-548b-a870-fa4256232163",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Masquerain.Name",
    display_name="Masquerain",
    searchable_by=["Masquerain", "Stage 1", "Masquerain"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    family_id=283,
    abilities=[
        Attack(
            title="Panic-Prompting Pattern",
            game_text="Flip a coin until you get tails. For each heads, discard a random card from your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bug Buzz",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)