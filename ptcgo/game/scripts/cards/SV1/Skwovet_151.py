from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations


async def _nest_stash(ctx):
    """Once per turn: optionally put the whole hand on the bottom of the
    deck, drawing a card when any card went there."""
    if not await ctx.ask_yes_no(
            "Shuffle your hand and put it on the bottom of your deck?"):
        return
    if await ctx.hand_to_bottom_of_deck(ctx.player_id):
        await ctx.draw_cards(1)

card = PokemonCardDef(
    guid="627a21a5-7595-5e27-b90f-c0db14199344",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skwovet.Name",
    display_name="Skwovet",
    searchable_by=["Skwovet", "Basic", "Skwovet"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=819,
    abilities=[
        Ability(
            title="Nest Stash",
            game_text="Once during your turn, you may shuffle your hand and put it on the bottom of your deck. If you put any cards on the bottom of your deck in this way, draw a card.",
            activation=Activations.ONCE_PER_TURN,
            effect=_nest_stash,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)