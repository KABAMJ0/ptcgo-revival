from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4c20eddf-46bf-5cb5-8ec3-b92536675d7b",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTusk.Name",
    display_name="Great Tusk",
    searchable_by=["Great Tusk", "Basic", "Ancient", "GreatTusk"],
    subtypes=["Basic", "Ancient"],
    collector_number=97,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Land Collapse",
            game_text="Discard the top card of your opponent's deck. If you played an Ancient Supporter card from your hand during this turn, discard 3 more cards in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Giant Tusk",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)