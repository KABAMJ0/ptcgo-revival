from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.attributes import AttrID


def _energy_connect_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    if board.active_pokemon(player_id) is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(is_basic_energy_card(energy)
               for benched in (bench.children if bench else [])
               for energy in board.attached_energies(benched))


async def _lightning_strike(ctx):
    lightning = [energy for energy in ctx.attached_energies(ctx.attacker)
                 if energy_provides_type(energy, PokemonTypes.LIGHTNING.value)]
    used = bool(lightning) and await ctx.ask_yes_no(
        "Discard all Lightning Energy cards attached to Ampharos?")
    if used:
        await ctx.discard_cards(lightning)
    await ctx.deal_damage(80 if used else 40)


card = PokemonCardDef(
    guid="2a53bf50-7402-591e-96d9-99c705dd4e98",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Energy Connect",
            game_text="As often as you like during your turn (before your attack), you may take a basic Energy card attached to 1 of your Benched Pok\u00e9mon and attach it to your Active Pok\u00e9mon. This power can't be used if Ampharos is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_energy_connect_available,
            effect=move_energy_between(is_basic_energy_card, count=1, from_pool="bench", to_pool="active"),
        ),
        Attack(
            title="Lightning Strike",
            game_text="You may discard all Lightning Energy cards attached to Ampharos. If you do, this attack's base damage is 80 instead of 40.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_lightning_strike,
        ),
    ],
)