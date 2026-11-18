from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="16f82051-0619-5eb2-875d-c40c256d896e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkraiG.Name",
    display_name="Darkrai G",
    searchable_by=["Darkrai G", "Basic", "SP", "DarkraiG"],
    subtypes=["Basic", "SP"],
    collector_number=3,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Ability(
            title="Eerie Aura",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon that remains Asleep between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Sleep",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, that Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)