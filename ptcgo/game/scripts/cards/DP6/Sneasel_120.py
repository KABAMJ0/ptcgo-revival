from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, TrainerType


async def _look_then_bin_tools(ctx):
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    tools = [card for card in ctx.hand(ctx.opponent_id)
             if card.get_attribute(AttrID.TRAINER_TYPE) in (
                 TrainerType.POKEMON_TOOL.value,
                 TrainerType.POKEMON_TOOL_F.value,
                 TrainerType.TECHNICAL_MACHINE.value)]
    if not tools:
        return
    for card in tools:
        await ctx.put_on_top_of_deck(card)
    await ctx.shuffle_deck(ctx.opponent_id)

card = PokemonCardDef(
    guid="86e54be5-e3e3-5852-b6da-deb359bff2ee",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    display_name="Sneasel",
    searchable_by=["Sneasel", "Basic", "Sneasel"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Rob",
            game_text="Look at your opponent's hand. If your opponent has any Pok\u00e9mon Tool or Technical Machine cards in his or her hand, put those cards on top of his or her deck. Your opponent shuffles his or her deck afterward.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=_look_then_bin_tools,
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)