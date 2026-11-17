from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8948eef7-2747-50d5-abbe-c34b4c373b42",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    display_name="Phantump",
    searchable_by=["Phantump", "Basic", "Phantump"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=708,
    abilities=[
        Ability(
            title="Spiteful Evolution",
            game_text="Once during your turn, you may use this Ability. Choose a card in your hand that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. If you do, place 2 damage counters on the Pok\u00e9mon you evolved in this way. You can't use this Ability during your first turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)