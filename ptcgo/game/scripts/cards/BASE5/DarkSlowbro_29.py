from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.data_utils import Triggers
from ptcgo.game.session.effects import is_basic_pokemon, is_evolution_pokemon


def _basic_or_evolution(card):
    return is_basic_pokemon(card) or is_evolution_pokemon(card)


async def reel_in(ctx):
    """When played, up to 3 Basic Pokemon and/or Evolution cards come back from
    the discard pile."""
    await recover_from_discard(_basic_or_evolution, count=3, minimum=0,
                               prompt="Choose up to 3 Basic Pokemon or Evolution cards")(ctx)

card = PokemonCardDef(
    guid="299e1c9e-40d9-5389-bdea-bb93cc857d12",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowbro.Name",
    display_name="Dark Slowbro",
    searchable_by=["Dark Slowbro", "Stage 1", "DarkSlowbro"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="BASE5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Reel In",
            game_text="When you play Dark Slowbro from your hand, choose up to 3 Basic Pok\u00e9mon and/or Evolution cards from your discard pile and put them into your hand.",
            trigger=Triggers.ON_PLAY,
            effect=reel_in,
        ),
        Attack(
            title="Fickle Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=flip_or_nothing(),
        ),
    ],
)