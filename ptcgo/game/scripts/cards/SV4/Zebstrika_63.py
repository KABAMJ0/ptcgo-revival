from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_prizes_taken, recoil_attack
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _basic_lightning_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) \
        and PokemonTypes.LIGHTNING.value in types


async def _burst_of_braying(ctx):
    """Attach Basic Lightning Energy from the discard, up to the prizes the
    opponent has taken, distributed as the player likes."""
    limit = count_prizes_taken("opponent")(ctx)
    cards = [c for c in ctx.discard_pile() if _basic_lightning_energy(c)]
    if not cards or limit <= 0:
        return
    picks = await ctx.choose_cards(
        cards, min(limit, len(cards)), minimum=0,
        prompt="Choose Basic Lightning Energy cards to attach.",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())

card = PokemonCardDef(
    guid="d171c461-9fd7-52ec-99ff-acd4c7f8841a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Zebstrika"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Burst of Braying",
            game_text="Choose Basic Lightning Energy cards from your discard pile up to the number of Prize cards your opponent has taken and attach them to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_burst_of_braying,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=recoil_attack(50),
        ),
    ],
)