from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.pokemon import energy_provides_type

async def _frozen_breath(ctx):
    await ctx.deal_damage()
    energies = [energy for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.WATER.value)]
    if len(energies) < 2:
        return
    if not await ctx.ask_yes_no(
            "Discard 2 Water Energy from this Pok\u00e9mon?"):
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 2,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.WATER.value),
        prompt="Choose 2 Water Energy to discard")
    if not discarded:
        return
    target = ctx.opponent_active()
    if target is not None:
        await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="8184ddae-4d9d-5991-a90f-3e4632a2e260",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=35,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Hail",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=spread_damage(20, side="opponent"),
        ),
        Attack(
            title="Frozen Breath",
            game_text="You may discard 2 Water Energy from this Pok\u00e9mon. If you do, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=_frozen_breath,
        ),
    ],
)