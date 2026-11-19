from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.data_utils import subtypes_for


def _is_baby(card):
    return "Baby" in (subtypes_for(card.archetype_id) or [])


async def lets_play(ctx):
    """Search the deck for a Baby Pokemon and put it onto your Bench."""
    await search_to_bench(_is_baby, count=1,
                          prompt="Choose a Baby Pokemon to put onto your Bench.")(ctx)

card = PokemonCardDef(
    guid="637e27da-7edd-503d-8def-448aeae88927",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu",
    searchable_by=["Pichu", "Baby", "Pichu"],
    subtypes=["Baby"],
    collector_number=35,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=172,
    abilities=[
        Attack(
            title="Let's Play!",
            game_text="Search your deck for a Baby Pok\u00e9mon card and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lets_play,
        ),
    ],
)