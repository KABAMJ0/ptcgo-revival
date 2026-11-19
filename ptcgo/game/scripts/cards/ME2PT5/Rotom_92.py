from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import named
from ptcgo.game.card_effects.attacks_common import damage_per


def _my_tools(ctx):
    return sum(
        1 for tool, pokemon in ctx.tools_in_play()
        if pokemon.owning_player_id == ctx.player_id
    )


card = PokemonCardDef(
    guid="9c96396a-bfdb-52ad-8524-b4fbc14da99f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Roto Call",
            game_text="You may search your deck for any number of Pok\u00e9mon that have \"Rotom\" in their name and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(named("rotom"), count=5),
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(_my_tools, 30),
        ),
    ],
)