from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.pokemon import in_active_spot


async def counterattack(ctx):
    """Active Spot only: if damaged by an opponent's attack (even if
    Knocked Out), put 3 damage counters on the Attacking Pokemon."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="9c3eac51-b720-5fc3-bbc6-e9626c5ae56a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic", "Cacnea"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=331,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=counterattack,
        ),
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)