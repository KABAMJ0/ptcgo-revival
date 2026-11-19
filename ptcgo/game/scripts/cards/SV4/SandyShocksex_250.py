from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.trainers import basic_energy_of

def _opponent_prizes_left(board, player_id):
    opponents = [pid for pid in board.player_ids if pid != player_id]
    if not opponents:
        return 6
    area = board.find_player_area(opponents[0], "prizePile")
    return len(area.children) if area else 6


def _four_or_fewer_left(board, player_id, pokemon):
    return _opponent_prizes_left(board, player_id) <= 4


async def _magnetic_absorption(ctx):
    """Attach a Basic Fighting Energy from the discard pile to this Pokemon."""
    pool = [card for card in ctx.discard_pile() if basic_energy_of("fighting")(card)]
    if not pool:
        return
    picks = await ctx.choose_cards(
        pool, 1, minimum=1,
        prompt="Choose a Basic Fighting Energy to attach")
    if picks:
        await ctx.attach_energy(picks[0], ctx.source)

card = PokemonCardDef(
    guid="cb0c405e-5d4c-5d79-9a57-a1c59abf39db",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SandyShocksex.Name",
    display_name="Sandy Shocks ex",
    searchable_by=["Sandy Shocks ex", "Basic", "ex", "Ancient", "SandyShocksex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=250,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=989,
    abilities=[
        Ability(
            title="Magnetic Absorption",
            game_text="Once during your turn, if your opponent has 4 or fewer Prize cards remaining, you may attach a Basic Fighting Energy card from your discard pile to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_four_or_fewer_left,
            effect=_magnetic_absorption,
        ),
        Attack(
            title="Earthen Spike",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=lock_self_attack(),
        ),
    ],
)