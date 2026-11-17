from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="859d24e5-fd07-5e1e-9e6b-5fff8463f0c7",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhex.Name",
    display_name="Ho-Oh ex",
    searchable_by=["Ho-Oh ex", "Basic", "ex", "HoOhex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP3",
    rarity=Rarities.Rare,
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