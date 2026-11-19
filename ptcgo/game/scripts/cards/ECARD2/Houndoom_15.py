from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import ability_lock_passive
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _burn_up(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Burn Up")
    if results and not results[0]:
        fire = [energy for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.FIRE.value)]
        if fire:
            await ctx.discard_cards(fire)


async def _dark_impact(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    ctx.add_passive_through_opponents_turn(
        defender, ability_lock_passive(lambda pokemon, carrier: pokemon is defender))


card = PokemonCardDef(
    guid="de8a20ef-fccf-5e4e-a832-d875538f4510",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Fireworks",
            game_text="Flip a coin. If tails, discard a Fire Energy card attached to Houndoom.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Dark Impact",
            game_text="The Defending Pok\u00e9mon can't use any Pok\u00e9-Powers until the end of your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_dark_impact,
        ),
    ],
)