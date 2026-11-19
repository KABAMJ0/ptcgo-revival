from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.pokemon import in_active_spot
from ptcgo.game.attributes import AttrID


async def counterattack(ctx):
    """If Active and damaged by an attack (even if KO'd): 3 counters on the attacker."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(30, target=attacker, apply_modifiers=False, as_counters=True)


async def spiky_storm(ctx):
    """100 damage (no W/R) to each opposing Pokemon that has damage counters."""
    for pokemon in list(ctx.opponent_pokemon_in_play()):
        max_hp = ctx.max_hp(pokemon)
        if (pokemon.get_attribute(AttrID.HP) or max_hp) < max_hp:
            await ctx.deal_damage(100, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="e2782bde-c28e-5792-a546-3c3d2c38bd3d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslashGX.Name",
    display_name="Alolan Sandslash-GX",
    searchable_by=["Alolan Sandslash-GX", "Stage 1", "GX", "AlolanSandslashGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=236,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    family_id=28,
    abilities=[
        Ability(
            title="Spiky Shield",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=counterattack,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
        Attack(
            title="Spiky Storm-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon that has any damage counters on it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=spiky_storm,
        ),
    ],
)