from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a87ce684-89ab-5ad5-ad40-47c69bf4e1b6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYuex.Name",
    display_name="Chi-Yu ex",
    searchable_by=["Chi-Yu ex", "Basic", "ex", "ChiYuex"],
    subtypes=["Basic", "ex"],
    collector_number=234,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Jealously Singe",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Flame Surge",
            game_text="Choose up to 3 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a Basic Fire Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)