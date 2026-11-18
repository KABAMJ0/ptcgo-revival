from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="12ddac57-f874-5317-b639-91c983d897f0",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=226,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Ability(
            title="Damp",
            game_text="Pok\u00e9mon in play (both yours and your opponent's) lose any Ability that requires the Pok\u00e9mon using it to Knock Out itself.",
            effect=unimplemented,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)