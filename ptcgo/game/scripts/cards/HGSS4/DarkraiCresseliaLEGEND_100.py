from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c7b7cc9-4ce3-53c0-9ada-11f3304874de",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiCresseliaLEGEND.Name",
    display_name="Darkrai & Cresselia LEGEND",
    searchable_by=["Darkrai & Cresselia LEGEND", "LEGEND", "DarkraiCresseliaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=100,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=488,
    abilities=[
        Attack(
            title="Lost Crisis",
            game_text="Choose 2 Energy attached to Darkrai & Cresselia LEGEND and put them in the Lost Zone. If any of your opponent's Pok\u00e9mon would be Knocked Out by damage from this attack, put that Pok\u00e9mon and all cards attached to it in the Lost Zone instead of discarding it.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
        Attack(
            title="Moon's Invite",
            game_text="Move as many damage counters on your opponent's Pok\u00e9mon as you like to any of your opponent's other Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)