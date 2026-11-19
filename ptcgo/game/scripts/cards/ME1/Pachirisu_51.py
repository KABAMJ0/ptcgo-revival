from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_TEXT = ("During your opponent's next turn, whenever they attach an Energy card "
         "from their hand to the Defending Pok\u00e9mon, place 8 damage counters "
         "on that Pok\u00e9mon.")


async def electrified_incisors(ctx):
    """10 damage. The rest of the printed text is the attach watch: the
    Ability below answers an Energy the opponent attaches from hand to their
    Active during their next turn while this attack is the last one used."""
    await ctx.deal_damage()


async def electrified_incisors_watch(ctx):
    """An attach from the opponent's hand to their Active lands 8 counters."""
    if not ctx.attack_used_last_turn(title="Electrified Incisors", entity=ctx.source):
        return
    if ctx.attaching_player_id != ctx.opponent_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None or receiver is not ctx.opponent_active():
        return
    await ctx.deal_damage(80, target=receiver, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="884321a2-1100-59fb-84b4-3292001e4f57",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Attack(
            title="Electrified Incisors",
            game_text=_TEXT,
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=electrified_incisors,
        ),
        Ability(
            title="Electrified Incisors",
            game_text=_TEXT,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=electrified_incisors_watch,
        ),
    ],
)