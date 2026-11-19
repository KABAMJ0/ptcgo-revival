from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import is_lightning_energy, is_energy_card

async def cluster_bolt(ctx):
    """70; discarding all Lightning Energy also puts 20 on every Benched
    opponent Pokemon that has Energy attached."""
    await ctx.deal_damage(70)
    attached = [energy for energy in ctx.attached_energies(ctx.attacker)
                if is_lightning_energy(energy)]
    if not attached:
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, len(attached), predicate=is_lightning_energy)
    if not discarded:
        return
    for pokemon in ctx.opponent_bench():
        if any(is_energy_card(card) for card in ctx.attached_energies(pokemon)):
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b92d9d18-37c1-565e-a32f-b0648df54206",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="POP7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Jamming",
            game_text="After your opponent plays a Supporter card from his or her hand, put 1 damage counter on each of your opponent's Pok\u00e9mon. You can't use more than 1 Jamming Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Cluster Bolt",
            game_text="You may discard all Lightning Energy attached to Ampharos. If you do, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any Energy cards attached to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=cluster_bolt,
        ),
    ],
)