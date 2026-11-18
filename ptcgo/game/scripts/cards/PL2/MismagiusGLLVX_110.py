from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5df8d12c-b004-583f-96b8-c9409a50c6ab",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MismagiusGLLVX.Name",
    display_name="Mismagius GL LV.X",
    searchable_by=["Mismagius GL LV.X", "Level-Up", "SP", "MismagiusGLLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=110,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MismagiusGL.Name",
    family_id=429,
    abilities=[
        Ability(
            title="Magical Return",
            game_text="As often as you like during your turn (before your attack), you may return a Pok\u00e9mon Tool or Technical Machine card attached to your Pok\u00e9mon to your hand. This power can't be used if Mismagius GL is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Magic",
            game_text="Count the number of cards in your hand. Put that many damage counters on the Defending Pok\u00e9mon. You can't put more than 8 damage counters in this way.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)