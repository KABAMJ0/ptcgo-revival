from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _fire_blow(ctx):
    fire = [energy for energy in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(energy, PokemonTypes.FIRE.value)]
    picks = []
    if fire:
        picks = await ctx.choose_cards(
            fire, len(fire), minimum=0,
            prompt="Discard any number of Fire Energy cards attached to Arcanine")
        if picks:
            await ctx.discard_cards(picks)
    heads = 0
    if picks:
        results = await ctx.flip_coins(len(picks), "Fire Blow")
        heads = sum(1 for result in results if result)
    await ctx.deal_damage(30 + 30 * heads)


card = PokemonCardDef(
    guid="4d6e3711-4a8f-5eaf-b91b-34cf6ec45d07",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1", "Arcanine"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Ability(
            title="Extreme Speed",
            game_text="You pay Colorless less to retreat Arcanine for each Energy attached to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Fire Blow",
            game_text="You may discard any number of Fire Energy cards attached to Arcanine when you use this attack. If you do, flip a number of coins equal to the number of Fire Energy cards you discarded. This attack does 30 damage plus 30 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)