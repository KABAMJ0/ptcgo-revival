from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon


class _SteelCoating(Passive):
    """Metal Energy on Probopass cuts attack damage by 10 each, capped at 20."""

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.target is not carrier_pokemon(carrier):
            return
        metal = sum(1 for energy in calc.board.attached_energies(calc.target)
                    if energy_provides_type(energy, PokemonTypes.METAL.value))
        calc.amount = max(0, calc.amount - min(20, 10 * metal))


async def _metal_bomber(ctx):
    await ctx.deal_damage()
    metal = sum(1 for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.METAL.value))
    bench = ctx.opponent_bench()
    allowed = min(metal, len(bench))
    if allowed <= 0:
        return
    picks = await ctx.choose_cards(
        bench, allowed, minimum=0,
        prompt=f"Choose up to {allowed} of your opponent's Benched Pokémon")
    for target in picks:
        await ctx.deal_damage(20, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="2c575021-76ed-54fb-9d6d-ad56f3d5d0c2",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Ability(
            title="Steel Coating",
            game_text="Any damage done to Probopass by your opponent's attacks is reduced by 10 for each Metal Energy attached to Probopass (after applying Weakness and Resistance). You can't reduce more than 20 damage in this way.",
            passive=_SteelCoating(),
        ),
        Attack(
            title="Metal Bomber",
            game_text="Choose a number of your opponent's Benched Pok\u00e9mon up to the amount of Metal Energy attached to Probopass. This attack does 20 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_metal_bomber,
        ),
    ],
)