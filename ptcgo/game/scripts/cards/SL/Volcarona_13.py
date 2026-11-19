from ptcgo.game.card_effects.support_common import opponent_switches
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def heat_cyclone_condition(board, player_id, pokemon):
    for other_id in board.player_ids:
        if other_id == player_id:
            continue
        bench = board.find_player_area(other_id, "bench")
        if bench is not None and bench.children:
            return True
    return False


async def heat_cyclone(ctx):
    if not await ctx.ask_yes_no(
            "Have your opponent switch their Active Pokémon?"):
        return False
    return await opponent_switches(ctx) is not None

card = PokemonCardDef(
    guid="358e25b7-fe8c-5daf-b70e-9f5b65369acf",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SL",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Ability(
            title="Heat Cyclone",
            game_text="Once during your turn (before your attack), you may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=heat_cyclone_condition,
            effect=heat_cyclone,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)