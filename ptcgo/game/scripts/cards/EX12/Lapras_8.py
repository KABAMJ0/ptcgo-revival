from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import on_bench_play
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import Triggers
from ptcgo.game.attributes import AttrID, TrainerType

def _is_supporter(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value


async def support_navigation(ctx):
    """Search the deck for a Supporter, show it, and put it into hand."""
    await search_to_hand(_is_supporter, count=1, reveal=True)(ctx)


card = PokemonCardDef(
    guid="5bd2e035-4a66-5caa-a61d-209ba46b2619",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=131,
    abilities=[
        Ability(
            title="Support Navigation",
            game_text="Once during your turn, when you put Lapras onto your Bench from your hand, you may search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_PLAY,
            effect=on_bench_play(support_navigation),
        ),
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)