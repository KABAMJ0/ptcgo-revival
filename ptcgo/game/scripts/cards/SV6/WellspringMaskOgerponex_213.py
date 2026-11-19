from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

async def _torrential_pump(ctx):
    """Printed damage to the Active; optionally shuffle 3 of this Pokemon's
    Energy in for 120 more to one of the opponent's Benched Pokemon."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.source)
    if len(energies) < 3:
        return
    if not await ctx.ask_yes_no(
        "Shuffle 3 Energy into your deck to also do 120 to a Benched Pokémon?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 3, minimum=3, prompt="Choose 3 Energy to shuffle into your deck")
    if not picks:
        return
    await ctx.shuffle_into_deck(picks)
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(120, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="8a7a3deb-1d42-5437-82b1-1f6eb24f5ec6",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerponex.Name",
    display_name="Wellspring Mask Ogerpon ex",
    searchable_by=["Wellspring Mask Ogerpon ex", "Basic", "Tera", "ex", "WellspringMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=213,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Sob",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Torrential Pump",
            game_text="You may shuffle 3 Energy attached to this Pok\u00e9mon into your deck. If you do, this attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=_torrential_pump,
        ),
    ],
)