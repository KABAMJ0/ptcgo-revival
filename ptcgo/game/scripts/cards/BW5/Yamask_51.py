from ptcgo.game.card_effects.attacks_common import flip_gate, random_card_to_deck
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _astonish(ctx):
    """Printed 10; on heads one card at random leaves the opponent's hand,
    is revealed, and is shuffled into their deck."""
    await ctx.deal_damage()
    await flip_gate(random_card_to_deck(damage=0))(ctx)


card = PokemonCardDef(
    guid="fa49bbf0-251c-52b4-9898-f23f860b3b97",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a card at random from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_astonish,
        ),
    ],
)