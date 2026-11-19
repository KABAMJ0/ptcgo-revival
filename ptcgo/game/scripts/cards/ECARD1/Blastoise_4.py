from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.attributes import AttrID


def _jet_stream_available(board, player_id, pokemon):
    return is_in_active_spot(pokemon) and not pokemon.get_attribute(
        AttrID.SPECIAL_CONDITIONS)


async def _jet_stream(ctx):
    results = await ctx.flip_coins(1, "Jet Stream")
    if not (results and results[0]):
        return
    await ctx.discard_energy_from(
        ctx.attacker, 1, prompt="Discard an Energy card attached to Blastoise")
    defender = ctx.defender
    if defender is not None:
        await ctx.discard_energy_from(
            defender, 1,
            prompt="Discard an Energy card attached to the Defending Pokémon")


card = PokemonCardDef(
    guid="21a4ec20-50d6-5854-a009-6e803db90b99",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Jet Stream",
            game_text="Once during your turn (before your attack), if Blastoise is your Active Pok\u00e9mon, you may flip a coin. If heads, discard an Energy card attached to Blastoise, if any. Then, if there are any Energy cards attached to the Defending Pok\u00e9mon, choose 1 of them and discard it. This power can't be used if Blastoise is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_jet_stream_available,
            effect=_jet_stream,
        ),
        Attack(
            title="Energy Cannon",
            game_text="Does 40 damage plus 10 more damage for each Energy attached to Blastoise but not used to pay for this attack's Energy Cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=damage_per_extra_energy(10, cap=20, base=40),
        ),
    ],
)