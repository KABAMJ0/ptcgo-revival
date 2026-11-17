from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fde235fd-79d4-5e9f-93dc-fd90743ab874",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Attack(
            title="Magnetic Lines",
            game_text="Flip a coin. If heads, move a basic Energy card from the Defending Pok\u00e9mon to another of your opponent's Pok\u00e9mon. (Ignore this effect if your opponent has only 1 Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)