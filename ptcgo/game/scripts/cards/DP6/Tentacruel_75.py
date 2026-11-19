from ptcgo.game.card_effects.attacks_common import conditions_if
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _tentacle_strike(ctx):
    energies = [card for card in ctx.discard_pile(ctx.opponent_id)
                if is_energy_card(card)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=0,
        prompt="Choose up to 2 Energy cards from your opponent's discard pile")
    targets = ctx.opponent_pokemon_in_play()
    for card in picks:
        target = await ctx.choose_pokemon(
            targets, "Choose an opponent's Pokémon to attach the Energy to")
        if target is None:
            continue
        if not await ctx.attach_energy(card, target):
            continue
        await ctx.deal_damage(20, target=target, apply_modifiers=False)


def _less_energy_than_defender(ctx) -> bool:
    defender, attacker = ctx.defender, ctx.attacker
    if defender is None or attacker is None:
        return False
    return len(ctx.attached_energies(attacker)) < len(ctx.attached_energies(defender))

card = PokemonCardDef(
    guid="166d08ad-77b9-5859-9f29-75f32e4ef36f",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Attack(
            title="Tentacle Strike",
            game_text="Search your opponent's discard pile for up to 2 Energy cards and attach them to any of your opponent's Pok\u00e9mon in any way you like. For each Energy card attached in this way, this attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={},
            effect=_tentacle_strike,
        ),
        Attack(
            title="Dangerous Poison",
            game_text="If Tentacruel has less Energy attached to it than the Defending Pok\u00e9mon, the Defending Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=conditions_if(_less_energy_than_defender,
                                 SpecialConditions.PARALYZED,
                                 SpecialConditions.POISONED),
        ),
    ],
)