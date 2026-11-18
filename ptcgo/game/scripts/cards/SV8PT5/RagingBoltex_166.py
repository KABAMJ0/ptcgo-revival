from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="540cc97e-32db-5d04-9336-2cfdcd3db62a",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBoltex.Name",
    display_name="Raging Bolt ex",
    searchable_by=["Raging Bolt ex", "Basic", "ex", "Ancient", "RagingBoltex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=166,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=240,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    abilities=[
        Attack(
            title="Burst Roar",
            game_text="Discard your hand and draw 6 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bellowing Thunder",
            game_text="You may discard any amount of Basic Energy from your Pok\u00e9mon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)