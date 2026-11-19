from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import distribute_energy
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card, is_psychic_energy_card,
)


def _basic_psychic_energy(card):
    return is_basic_energy_card(card) and is_psychic_energy_card(card)


async def _transfer_charge(ctx):
    """Attach up to 2 Basic Psychic Energy from the discard, distributed."""
    cards = [c for c in ctx.discard_pile() if _basic_psychic_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Choose up to 2 Basic Psychic Energy cards to attach.",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="18482cb5-3963-55a2-bc80-308a537de733",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwoex.Name",
    display_name="Mewtwo ex",
    searchable_by=["Mewtwo ex", "Basic", "Tera", "ex", "Mewtwoex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=58,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Transfer Charge",
            game_text="Attach up to 2 Basic Psychic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_transfer_charge,
        ),
        Attack(
            title="Photon Kinesis",
            game_text="This attack does 30 more damage for each Psychic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy('mine', energy_type=PokemonTypes.PSYCHIC), 30, base=10),
        ),
    ],
)