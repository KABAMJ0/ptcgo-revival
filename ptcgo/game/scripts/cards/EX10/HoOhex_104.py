from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b915bd06-eed1-5106-8c30-7ac299a63a37",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhex.Name",
    display_name="Ho-Oh ex",
    searchable_by=["Ho-Oh ex", "Basic", "ex", "HoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=104,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Wing",
            game_text="If Ho-Oh ex would be Knocked Out by damage from an opponent's attack, you may move up to 2 Energy attached to Ho-Oh ex to your Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 10 damage plus 20 more damage for each type of basic Energy card attached to Ho-Oh ex.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)