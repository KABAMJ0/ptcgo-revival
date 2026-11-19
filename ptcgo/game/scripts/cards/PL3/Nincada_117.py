from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="8d765c1a-5da9-5d77-9f2c-5006ade352f2",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    display_name="Nincada",
    searchable_by=["Nincada", "Basic", "Nincada"],
    subtypes=["Basic"],
    collector_number=117,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=290,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=1),
        ),
        Attack(
            title="Dash Attack",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)