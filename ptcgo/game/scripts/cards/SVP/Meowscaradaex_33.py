from ptcgo.game.card_effects.attacks_common import bonus_if, has_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import requires_hand
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card, is_grass_energy_card,
)


def _basic_grass_energy(card):
    return is_basic_energy_card(card) and is_grass_energy_card(card)


_bouquet_gate = requires_hand(_basic_grass_energy, n=1)


async def _bouquet_magic(ctx):
    """Discard a Basic Grass Energy from hand, then 3 counters on their Bench."""
    if not await ctx.ask_yes_no(
            "Discard a Basic Grass Energy card from your hand?"):
        return
    if not await ctx.discard_from_hand(
            1, predicate=_basic_grass_energy,
            prompt="Discard a Basic Grass Energy card"):
        return
    bench = ctx.opponent_bench()
    if bench:
        await ctx.place_damage_counters(3, bench)

card = PokemonCardDef(
    guid="8f40cd71-fce7-5fda-beb7-04c3b149502e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowscaradaex.Name",
    display_name="Meowscarada ex",
    searchable_by=["Meowscarada ex", "Stage 2", "ex", "Meowscaradaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=33,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=310,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    family_id=906,
    abilities=[
        Ability(
            title="Bouquet Magic",
            game_text="You must discard a Basic Grass Energy card from your hand in order to use this Ability. Once during your turn, you may put 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_bouquet_gate,
            effect=_bouquet_magic,
        ),
        Attack(
            title="Scratching Nails",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(has_damage("defender"), 120),
        ),
    ],
)