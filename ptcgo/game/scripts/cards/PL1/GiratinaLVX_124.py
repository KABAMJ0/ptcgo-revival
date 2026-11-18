from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="578664f5-45a1-590b-a6b8-576b11d411fd",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaLVX.Name",
    display_name="Giratina LV.X",
    searchable_by=["Giratina LV.X", "Level-Up", "GiratinaLVX"],
    subtypes=["Level-Up"],
    collector_number=124,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    family_id=487,
    abilities=[
        Ability(
            title="Invisible Tentacles",
            game_text="Whenever your opponent's Pok\u00e9mon tries to attack, your opponent discards 1 card from his or her hand. (If your opponent can't discard 1 card, your opponent's Pok\u00e9mon can't attack.) You can't use more than 1 Invisible Tentacles Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Lost",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If any of your opponent's Pok\u00e9mon would be Knocked Out by damage from this attack, put that Pok\u00e9mon and all cards attached to it in the Lost Zone instead of discarding it.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)