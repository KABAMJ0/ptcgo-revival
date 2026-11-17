from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7dbbbdaa-b374-5ce5-b724-4db0091367ae",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Energy Evolution",
            game_text="When you attach a basic Energy card from your hand to this Pok\u00e9mon during your turn, you may search your deck for a card that evolves from this Pok\u00e9mon that is the same type as that Energy card and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Quick Draw",
            game_text="Flip a coin. If heads, draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)