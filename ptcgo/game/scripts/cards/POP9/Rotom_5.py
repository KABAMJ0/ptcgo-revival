from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import AttrID, CardType, PokemonTypes, PokemonStage, Rarities

from ptcgo.game.session.passives import Passive, carrier_pokemon


class PsychicUntilEndOfTurnPassive(Passive):
    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is pokemon:
            return [PokemonTypes.PSYCHIC.value]
        return types

async def type_shift(ctx):
    """Rotom's type is Psychic until the end of this turn."""
    source = ctx.source
    if source is None:
        return
    ctx.add_temporary_passive(
        source, PsychicUntilEndOfTurnPassive(),
        expires_after_turn=ctx.session.turn_state.turn_number)


COUNTED = CardType.TRAINER.value


async def poltergeist(ctx):
    """Look at the opponent's hand: 30 plus 10 for each Trainer there."""
    await ctx.reveal_hand(ctx.opponent_id)
    counted = sum(1 for card in ctx.hand(ctx.opponent_id)
                  if card.get_attribute(AttrID.CARD_TYPE) == COUNTED)
    await ctx.deal_damage(30 + 10 * counted)


card = PokemonCardDef(
    guid="36343edc-1390-5d2f-9538-dc9bbdc8404f",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="POP9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Type Shift",
            game_text="Once during your turn (before your attack), you may use this power. Rotom's type is Psychic until the end of your turn.",
            activation=Activations.ONCE_PER_TURN,
            effect=type_shift,
        ),
        Attack(
            title="Poltergeist",
            game_text="Look at your opponent's hand. This attack does 30 damage plus 10 more damage for each Trainer, Supporter, and Stadium card in your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=poltergeist,
        ),
    ],
)