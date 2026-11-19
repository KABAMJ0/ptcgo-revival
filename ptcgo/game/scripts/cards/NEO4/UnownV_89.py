from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.support_common import entity_name
from ptcgo.game.session.effects import full_stack


def _unown_named(pokemon):
    return pokemon is not None and "Unown" in entity_name(pokemon)


async def _vanish(ctx):
    source = ctx.source
    results = await ctx.flip_coins(1, "Vanish")
    if not (results and results[0]):
        return
    others = [pokemon for pokemon in ctx.my_pokemon_in_play()
              if pokemon is not source and _unown_named(pokemon)]
    if not others:
        return
    pick = await ctx.choose_pokemon(others, "Choose an Unown to return to your hand")
    if pick is None:
        return
    was_active = pick is ctx.my_active()
    attachments = [card for card in full_stack(pick) if card is not pick]
    if attachments:
        await ctx.discard_cards(attachments)
    await ctx.put_in_hand([pick], reveal=True)
    if was_active:
        async def _promote():
            await ctx.session._promote_new_active(ctx.player_id)

        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="b3bacf6f-20ab-5ae2-aedc-ed8abfac48d8",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownV.Name",
    display_name="Unown [V]",
    searchable_by=["Unown [V]", "Basic", "UnownV"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Vanish]",
            trigger=Triggers.ON_PLAY,
            game_text="When you play Unown [V] from your hand, you may flip a coin. If heads, return 1 of your Pok\u00e9mon with Unown in its name (other than Unown [V]) to your hand. (Discard all cards attached to that card.)",
            effect=_vanish,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)