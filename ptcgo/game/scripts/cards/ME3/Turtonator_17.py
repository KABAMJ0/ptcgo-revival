from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.card_effects.pokemon import in_active_spot


async def shell_spikes(ctx):
    """Active Spot only: after being damaged by an attack (even if Knocked
    Out), discard an Energy from the Attacking Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None or ctx.effects_blocked(attacker):
        return
    await ctx.discard_energy_from(attacker, 1)


card = PokemonCardDef(
    guid="677c0ef6-05b9-5238-a1af-a608f0d978ca",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="ME3",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Ability(
            title="Shell Spikes",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), discard an Energy from the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=shell_spikes,
        ),
        Attack(
            title="Heat Breath",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)