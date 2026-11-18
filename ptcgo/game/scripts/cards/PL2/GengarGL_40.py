from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b11ce08-2d29-503c-9daf-8538d481e14d",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarGL.Name",
    display_name="Gengar GL",
    searchable_by=["Gengar GL", "Basic", "SP", "GengarGL"],
    subtypes=["Basic", "SP"],
    collector_number=40,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=94,
    abilities=[
        Attack(
            title="Confuse Ray",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Attack and Hide",
            game_text="Put 3 damage counters on 1 of your opponent's Pok\u00e9mon. You may shuffle Gengar GL and all cards attached to it back into your deck.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)