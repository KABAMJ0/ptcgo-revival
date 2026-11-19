from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def land_stream(ctx):
    """Printed 50, plus 20 for each basic Energy you discard from this Pokemon."""
    energies = [card for card in ctx.attached_energies(ctx.attacker)
                if is_basic_energy_card(card)]
    discarded = 0
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Discard any number of basic Energy cards from Team Magma's Aggron")
        if picks:
            await ctx.discard_cards(picks)
            discarded = len(picks)
    await ctx.deal_damage(50 + 20 * discarded)

card = PokemonCardDef(
    guid="3db597ad-2bef-5e66-ad50-31c4871c64dd",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAggron.Name",
    display_name="Team Magma's Aggron",
    searchable_by=["Team Magma's Aggron", "Stage 2", "TeamMagmasAggron"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIGHTING, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Crush",
            game_text="Flip a coin for each Energy attached to Team Magma's Aggron. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Land Stream",
            game_text="You may discard any number of basic Energy cards attached to Team Magma's Aggron. If you do, this attack does 50 damage plus 20 more damage for each basic Energy card you discarded.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=land_stream,
        ),
    ],
)