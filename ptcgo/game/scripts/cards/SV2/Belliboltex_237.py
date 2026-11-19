from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.attacks_common import snipe_attack


async def _paralyzing_ball(ctx):
    """Printed damage, then an optional discard of 2 Lightning Energy to Paralyze."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    defender = ctx.defender
    if attacker is None or defender is None:
        return
    attached = [e for e in ctx.attached_energies(attacker)
                if energy_provides_type(e, PokemonTypes.LIGHTNING.value)]
    if len(attached) < 2:
        return
    if not await ctx.ask_yes_no(
            "Discard 2 Lightning Energy to Paralyze the Defending Pokémon?"):
        return
    picks = await ctx.choose_cards(
        attached, 2, prompt="Choose 2 Lightning Energy to discard.")
    if len(picks) < 2:
        return
    await ctx.discard_cards(picks)
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="9ed17ff9-3804-5f52-bdc4-f78612ea51db",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Belliboltex.Name",
    display_name="Bellibolt ex",
    searchable_by=["Bellibolt ex", "Stage 1", "ex", "Belliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=237,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Attack(
            title="Jumping Press",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Paralyzing Ball",
            game_text="You may discard 2 Lightning Energy from this Pok\u00e9mon to make your opponent's Active Pok\u00e9mon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_paralyzing_ball,
        ),
    ],
)