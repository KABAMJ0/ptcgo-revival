from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.pokemon import in_active_spot


async def counterattack(ctx):
    """If Active and damaged by an attack (even if KO'd): 3 counters on the attacker."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="8dcfaed6-46e6-501f-9081-02d627e3db2d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name",
    display_name="Sharpedo",
    searchable_by=["Sharpedo", "Stage 1", "Sharpedo"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=counterattack,
        ),
        Attack(
            title="Aqua Impact",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 20, base=60),
        ),
    ],
)