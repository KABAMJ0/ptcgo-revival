from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def plunge_condition(board, player_id, pokemon):
    if pokemon is None or is_in_active_spot(pokemon):
        return False
    active = board.active_pokemon(player_id)
    return active is not None and bool(board.attached_energies(active))


async def plunge(ctx):
    me = ctx.source
    active = ctx.my_active()
    if me is None or active is None or me is active:
        return False
    energies = list(ctx.attached_energies(active))
    if not energies:
        return False
    moved = await ctx.move_energy_freely(
        [active], [me], max_count=len(energies),
        prompt="Move all Energy to this Pokémon",
    )
    if not moved:
        return False
    return await ctx.switch_active(ctx.player_id, me)

card = PokemonCardDef(
    guid="e2394dde-b4e7-5a80-9554-43e1aed781ae",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    display_name="Croconaw",
    searchable_by=["Croconaw", "Stage 1", "Croconaw"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SL",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name",
    family_id=158,
    abilities=[
        Ability(
            title="Plunge",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may move all Energy from your Active Pok\u00e9mon to this Pok\u00e9mon. If you do, switch it with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=plunge_condition,
            effect=plunge,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)