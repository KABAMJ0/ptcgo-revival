from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import unafflicted

async def _burning_energy(ctx):
    ctx.rewrite_energy_types(
        [PokemonTypes.FIRE.value], for_player=ctx.player_id, basic_only=True,
        through_turn=ctx.session.turn_state.turn_number)


async def _scorching_whirlwind(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(2, "Scorching Whirlwind")
    tails = sum(1 for result in results if not result)
    if tails == 0:
        return
    if tails == 1:
        await ctx.discard_energy_from(
            ctx.attacker, 2,
            prompt="Discard 2 Energy cards attached to Charizard")
    else:
        await ctx.discard_cards(ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="b3728429-611e-56b7-9ff1-350cb3272bf3",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Burning Energy",
            game_text="Once during your turn (before your attack), you may turn all basic Energy attached to all of your Pok\u00e9mon into Fire Energy for the rest of the turn. This power can't be used if Charizard is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_burning_energy,
        ),
        Attack(
            title="Scorching Whirlwind",
            game_text="Flip 2 coins. If 1 of them is tails, discard 2 Energy cards attached to Charizard. If both are tails, discard all Energy cards attached to Charizard.",
            cost={PokemonTypes.FIRE: 4},
            damage=120,
            effect=_scorching_whirlwind,
        ),
    ],
)