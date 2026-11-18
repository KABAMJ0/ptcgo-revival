from ptcgo.game.data_utils import StadiumCardDef, Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named
from ptcgo.game.models.board import PokemonEntity


def _is_arceus(card):
    return pokemon_named("arceus")(card)


def _ultimate_zone_ready(board, player_id, card=None):
    active = board.active_pokemon(player_id)
    if active is None or not _is_arceus(active):
        return False
    area = board.find_player_area(player_id, "bench")
    bench = [child for child in (area.children if area else [])
             if isinstance(child, PokemonEntity)]
    return any(board.attached_energies(pokemon) for pokemon in bench)


async def _ultimate_zone(ctx):
    active = ctx.my_active()
    if active is None or not _is_arceus(active):
        return
    sources = [pokemon for pokemon in ctx.my_bench()
               if ctx.attached_energies(pokemon)]
    if not sources:
        return
    await ctx.move_energy_freely(
        sources, [active], max_count=1,
        prompt="Choose an Energy to move to your Active Arceus")


card = StadiumCardDef(
    guid="b7f26af1-2eae-50c2-9563-c798e7f462b0",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltimateZone.Name",
    display_name="Ultimate Zone",
    searchable_by=["Ultimate Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Ultimate Zone",
        game_text="During each player's turn, the player may move an Energy "
                  "card attached to 1 of his or her Benched Pok\u00e9mon to his "
                  "or her Active Arceus as often as he or she likes.",
        activation=Activations.UNLIMITED,
        condition=_ultimate_zone_ready,
        effect=_ultimate_zone,
    )
)
