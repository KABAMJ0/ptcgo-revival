from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e4d739c2-e074-5eaa-a27f-781ac857c687",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Attack(
            title="Ominous News",
            game_text="Discard a Special Energy from 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dirty Throw",
            game_text="Discard a card from your hand. If you can't discard a card, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)