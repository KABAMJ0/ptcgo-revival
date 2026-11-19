from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.session.effects import is_pokemon_card


async def night_raid(ctx):
    """Printed 70; the opponent reveals their hand and you discard a Pokemon
    from it."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)
    candidates = [card for card in ctx.hand(ctx.opponent_id)
                  if is_pokemon_card(card)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1,
        prompt="Choose a Pokémon to discard from your opponent's hand")
    if picked:
        await ctx.discard_cards(picked)


card = PokemonCardDef(
    guid="6199f889-ea93-5a60-99e3-7fac205e3a87",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Night Raid",
            game_text="Your opponent reveals their hand. Discard a Pok\u00e9mon from it.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=night_raid,
        ),
    ],
)