from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.support_common import draw_until_effect


class SwirlingProsePassive(Passive):
    """While this Pokemon is Active, the opponent's new Active after a
    switch during their own turn becomes Confused."""

    async def on_active_switched(self, ctx, player_id, outgoing, incoming,
                                 outgoing_conditions, via_trainer, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not is_in_active_spot(holder):
            return
        if player_id == holder.owning_player_id:
            return
        if ctx.session.turn_state.active_player_id != player_id:
            return
        await ctx.apply_special_condition(incoming, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="670ec80c-ad80-5285-b4e8-e8e86cc6ac47",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagiusex.Name",
    display_name="Mismagius ex",
    searchable_by=["Mismagius ex", "Stage 1", "ex", "Mismagiusex"],
    subtypes=["Stage 1", "ex"],
    collector_number=112,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Swirling Prose",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, whenever your opponent's Active Pok\u00e9mon moves to the Bench during their turn, their new Active Pok\u00e9mon is now Confused.",
            passive=SwirlingProsePassive(),
        ),
        Attack(
            title="Hexa-Magic",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=150,
            effect=draw_until_effect(6, optional=True),
        ),
    ],
)