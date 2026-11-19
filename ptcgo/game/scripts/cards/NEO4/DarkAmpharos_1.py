from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _conductivity_condition(board, player_id, pokemon) -> bool:
    """"Stops working if you have more than 1 Dark Ampharos in play or while
    Dark Ampharos is Asleep, Confused, or Paralyzed."""
    if not unafflicted(board, player_id, pokemon):
        return False
    same_name = [p for p in board.pokemon_in_play(player_id)
                 if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "DarkAmpharos"]
    return len(same_name) <= 1


async def _conductivity(ctx):
    """Their hand attach to any Pokemon costs that Pokemon 10 (no W/R).

    The one-copy restriction is enforced here as well as in the condition:
    trigger resolution does not consult `condition`, so a second Dark Ampharos
    would otherwise fire the power again."""
    if ctx.attaching_player_id == ctx.player_id or ctx.energy_receiver is None:
        return
    if not _conductivity_condition(ctx.board, ctx.player_id, ctx.source):
        return
    await ctx.deal_damage(10, target=ctx.energy_receiver, apply_modifiers=False)

card = PokemonCardDef(
    guid="65009733-f597-5fb3-966c-b583ced886d6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAmpharos.Name",
    display_name="Dark Ampharos",
    searchable_by=["Dark Ampharos", "Stage 2", "DarkAmpharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Conductivity",
            game_text="Whenever your opponent attaches an Energy card from his or her hand to a Pok\u00e9mon, this power does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working if you have more than 1 Dark Ampharos in play or while Dark Ampharos is Asleep, Confused, or Paralyzed.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            condition=_conductivity_condition,
            effect=_conductivity,
        ),
        Attack(
            title="Shock Bolt",
            game_text="Discard all Lightning Energy cards attached to Dark Ampharos or this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)