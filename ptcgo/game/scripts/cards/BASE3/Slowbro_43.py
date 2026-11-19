from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import Activations
from ptcgo.game.session.passives import effective_max_hp


def _damaged_other(board, slowbro):
    return [p for p in board.pokemon_in_play(slowbro.owning_player_id)
            if p is not slowbro
            and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)]


def _strange_ready(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    return bool(_damaged_other(board, pokemon))


async def _strange_behavior(ctx):
    """Move 1 damage counter from one of your Pokemon to Slowbro, as long as
    it does not Knock Slowbro Out."""
    slowbro = ctx.attacker
    if slowbro is None or slowbro.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return
    if slowbro.get_attribute(AttrID.HP, 0) <= 10:
        return
    sources = _damaged_other(ctx.board, slowbro)
    if not sources:
        return
    source = sources[0] if len(sources) == 1 else await ctx.choose_pokemon(
        sources, "Choose a Pokemon to move a damage counter from")
    if source is None:
        return
    await ctx.move_damage_counters(source, slowbro, max_count=1)

card = PokemonCardDef(
    guid="535640a5-480a-5e13-9f11-5fcc572aa371",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=43,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Strange Behavior",
            game_text="As often as you like during your turn (before your attack), you may move 1 damage counter from 1 of your Pok\u00e9mon to Slowbro as long as you don't Knock Out Slowbro. This power can't be used if Slowbro is Asleep, Confused, or Paralyzed.",
            activation=Activations.UNLIMITED,
            condition=_strange_ready,
            effect=_strange_behavior,
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)