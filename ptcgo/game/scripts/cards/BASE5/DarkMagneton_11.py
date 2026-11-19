from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

from ptcgo.game.card_effects.trainers import is_basic_energy_card


async def magnetic_lines(ctx):
    """Printed 30; move a basic Energy off the Defending Pokemon onto one of
    their Benched Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or not bench:
        return
    energies = [e for e in ctx.attached_energies(defender) if is_basic_energy_card(e)]
    if not energies:
        return
    picks = await ctx.choose_cards(energies, 1, minimum=1,
                                   prompt="Choose a basic Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon to attach it to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)

card = PokemonCardDef(
    guid="6289380b-836e-5cfb-a512-5c22cb16a091",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagneton.Name",
    display_name="Dark Magneton",
    searchable_by=["Dark Magneton", "Stage 1", "DarkMagneton"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Sonicboom",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
        Attack(
            title="Magnetic Lines",
            game_text="If the Defending Pok\u00e9mon has any basic Energy cards attached to it, choose 1 of them. If your opponent has any Benched Pok\u00e9mon, choose 1 of them and attach that Energy card to it.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=30,
            effect=magnetic_lines,
        ),
    ],
)