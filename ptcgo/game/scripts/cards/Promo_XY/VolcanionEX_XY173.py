from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.attributes import AttrID

def _basic_fire(pokemon):
    from ptcgo.game.attributes import PokemonStage
    if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
        return False
    return PokemonTypes.FIRE.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


async def steam_up(ctx):
    """Discard a Fire Energy from hand; this turn your Basic Fire Pokemon's
    attacks do 30 more to the opponent's Active."""
    from ptcgo.game.card_effects.pokemon import energy_provides_type
    from ptcgo.game.session.passives import TurnDamageModifier
    fires = [c for c in ctx.hand() if energy_provides_type(c, PokemonTypes.FIRE.value)]
    if not fires:
        return
    picked = await ctx.choose_cards(fires, 1, prompt="Discard a Fire Energy")
    if not picked:
        return
    await ctx.discard_cards(picked)
    ctx.session.turn_state.damage_modifiers.append(
        TurnDamageModifier(30, ctx.player_id, opposing_active_only=True,
                           source_predicate=_basic_fire))


card = PokemonCardDef(
    guid="b9c10544-822c-5e6d-bae5-46da37ed64fb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VolcanionEX.Name",
    display_name="Volcanion-EX",
    searchable_by=["Volcanion-EX", "Basic", "EX", "VolcanionEX"],
    subtypes=["Basic", "EX"],
    collector_number=173,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE, PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Ability(
            title="Steam Up",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy card from your hand. If you do, during this turn, your Basic Fire Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            activation=Activations.ONCE_PER_TURN,
            effect=steam_up,
        ),
        Attack(
            title="Volcanic Heat",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=lock_self_attack(),
        ),
    ],
)