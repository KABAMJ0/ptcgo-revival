from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import requires_hand
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations

async def make_do(ctx):
    """Discard a card from your hand. Then, you may draw 2 cards."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card for Make Do"):
        return
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)

card = PokemonCardDef(
    guid="00186787-1b98-5c17-8692-3a41744d2d0c",
    key="SWSH12TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoir.Name",
    display_name="Gardevoir",
    searchable_by=["Gardevoir", "Stage 2", "Gardevoir"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SWSH12TG",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=282,
    abilities=[
        Ability(
            title="Refinement",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            effect=make_do,
            condition=requires_hand(n=1),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)