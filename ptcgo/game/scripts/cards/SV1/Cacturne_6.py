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
    guid="bab58b52-8f42-50c4-a6b0-69f3445499aa",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Counterattack Quills",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=counterattack,
        ),
        Attack(
            title="Spike Shot",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)