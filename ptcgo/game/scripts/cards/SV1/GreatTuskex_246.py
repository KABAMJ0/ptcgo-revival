from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c607ac1a-0b35-5d39-a643-84edccd17fb2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex", "GreatTuskex"],
    subtypes=["Basic", "ex"],
    collector_number=246,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Bedrock Breaker",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Gigantic Tusks",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=250,
            effect=unimplemented,
        ),
    ],
)