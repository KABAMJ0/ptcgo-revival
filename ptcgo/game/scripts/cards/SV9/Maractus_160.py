from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import Triggers


async def bursting_needles(ctx):
    """Active Spot only: if Knocked Out by damage from an opponent's
    attack, put 6 damage counters on the Attacking Pokemon."""
    if not ctx.ko_from_attack:
        return
    active_area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
    if active_area is not None and active_area.children:
        return  # was Benched, not Active, when Knocked Out
    attacker = ctx.ko_attacker
    if attacker is None:
        return
    await ctx.deal_damage(60, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="e6f24c59-af71-547d-926b-1717224a0c9f",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus", "Basic", "Maractus"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=556,
    abilities=[
        Ability(
            title="Exploding Needles",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, put 6 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=bursting_needles,
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
    ],
)