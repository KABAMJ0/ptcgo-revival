from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0e784987-3976-57c0-936f-47089758cdd9",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    display_name="Alakazam-EX",
    searchable_by=["Alakazam-EX", "Basic", "EX", "AlakazamEX"],
    subtypes=["Basic", "EX"],
    collector_number=125,
    set_code="XY10",
    rarity=Rarities.RareSecret,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Ability(
            title="Kinesis",
            game_text="When you play M Alakazam-EX from your hand to evolve this Pok\u00e9mon, before it evolves, you may put 2 damage counters on your opponent's Active Pok\u00e9mon and 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Suppression",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)