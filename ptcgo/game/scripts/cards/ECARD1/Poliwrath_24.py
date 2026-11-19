from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage
from ptcgo.game.card_effects.passives_common import is_in_active_spot


def _plunge_ready(board, player_id, pokemon) -> bool:
    return not is_in_active_spot(pokemon)


async def _plunge(ctx):
    poliwrath = ctx.source
    active = ctx.my_active()
    if active is None or active is poliwrath:
        return
    results = await ctx.flip_coins(1, "Plunge")
    if not (results and results[0]):
        return
    for energy in list(ctx.attached_energies(active)):
        await ctx.move_energy(energy, poliwrath)
    await ctx.switch_active(ctx.player_id, poliwrath)

card = PokemonCardDef(
    guid="bf21ff64-de86-5dab-a02b-d2518e3e1be7",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=24,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Plunge",
            game_text="Once during your turn (before your attack), if Poliwrath is on your Bench, you may flip a coin. If heads, take all Energy cards attached to your Active Pok\u00e9mon, if any, and attach them to Poliwrath. Then switch Poliwrath with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_plunge_ready,
            effect=_plunge,
        ),
        Attack(
            title="Water Punch",
            game_text="Flip a number of coins equal to the amount of Water Energy attached to Poliwrath. This attack does 40 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=flip_damage(coins_from=count_energy("self", PokemonTypes.WATER), base=40, per_heads=10),
        ),
    ],
)