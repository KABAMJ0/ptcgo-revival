from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="225b8014-927e-560d-9dd7-8fa82262249b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silvally.Name",
    display_name="Silvally",
    searchable_by=["Silvally", "Stage 1", "Silvally"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=772,
    abilities=[
        Ability(
            title="Call a Buddy",
            game_text="Once during your turn, if you have no cards in your hand, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Air Slash",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=unimplemented,
        ),
    ],
)