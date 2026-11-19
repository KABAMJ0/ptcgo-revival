from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_condition
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_condition

from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.passives import Passive


class ToxicSpikesPassive(Passive):
    """Whenever your opponent's Active Pokemon retreats, the Pokemon they
    switch in is now Poisoned."""

    async def on_active_switched(self, ctx, player_id, outgoing, incoming,
                                 outgoing_conditions, via_trainer):
        if incoming is None or incoming.owning_player_id == getattr(
                self, "owner_id", None):
            return
        await ctx.apply_special_condition(incoming, SpecialConditions.POISONED)


def _toxic_spikes():
    """Whenever your opponent's Active Pokemon retreats, their new Active
    Pokemon is Poisoned."""
    return ToxicSpikesPassive()

card = PokemonCardDef(
    guid="2033e680-f6c1-5611-a8c0-f5443ce6be46",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxapex.Name",
    display_name="Toxapex",
    searchable_by=["Toxapex", "Stage 1", "Toxapex"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    family_id=747,
    abilities=[
        Ability(
            title="Toxic Spikes",
            game_text="Whenever your opponent's Active Pok\u00e9mon retreats, their new Active Pok\u00e9mon is Poisoned.",
            passive=_toxic_spikes(),
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pok\u00e9mon is Poisoned, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(defender_has_condition(SpecialConditions.POISONED), 50),
        ),
    ],
)