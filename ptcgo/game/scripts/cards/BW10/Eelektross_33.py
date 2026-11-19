from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crush_and_burn(ctx) -> None:
    """Discard any number of your Energy cards; 30 damage each."""
    energies = [energy for pokemon in ctx.my_pokemon_in_play()
                for energy in ctx.attached_energies(pokemon)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Choose any number of Energy cards to discard")
    if not picks:
        return
    await ctx.discard_cards(list(picks))
    await ctx.deal_damage(30 * len(picks))


card = PokemonCardDef(
    guid="58927603-efc5-50f5-a266-9e55052c13e2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Team Plasma", "Eelektross"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=33,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Crush and Burn",
            game_text="Discard as many Energy attached to your Pok\u00e9mon as you like. This attack does 30 damage times the number of Energy cards you discarded.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=crush_and_burn,
        ),
        Attack(
            title="Thunder Tempest",
            game_text="Flip 4 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=50),
        ),
    ],
)