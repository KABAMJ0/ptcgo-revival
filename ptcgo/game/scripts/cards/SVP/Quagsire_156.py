from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b58e9e8a-c0b0-58c1-a47f-69d54dd85599",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1", "Quagsire"],
    subtypes=["Stage 1"],
    collector_number=156,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Drenched Headbutt",
            game_text="Discard the top 3 cards of your deck. This attack does 80 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)