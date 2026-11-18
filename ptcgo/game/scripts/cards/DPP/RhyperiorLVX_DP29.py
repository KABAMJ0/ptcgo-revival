from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c31f4d73-17f5-50ea-9fae-7200d3803289",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RhyperiorLVX.Name",
    display_name="Rhyperior LV.X",
    searchable_by=["Rhyperior LV.X", "Level-Up", "RhyperiorLVX"],
    subtypes=["Level-Up"],
    collector_number=29,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    family_id=464,
    abilities=[
        Attack(
            title="Hard Crush",
            game_text="Discard the top 5 cards from your deck. This attack does 50 damage for each Energy card you discarded.",
            cost={},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Upthrow",
            game_text="Search your discard pile for all Fighting Energy cards, show them to your opponent, and shuffle them into your deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)