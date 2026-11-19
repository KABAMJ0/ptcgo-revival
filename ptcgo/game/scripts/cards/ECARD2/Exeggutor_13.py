from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage

async def _lateral_eggsplosion(ctx):
    attached = sum(len(ctx.attached_energies(pokemon)) for pokemon in ctx.my_bench())
    heads = 0
    if attached:
        results = await ctx.flip_coins(attached, "Lateral Eggsplosion")
        heads = sum(1 for result in results if result)
    await ctx.deal_damage(30 + 10 * heads)


card = PokemonCardDef(
    guid="d733dc1c-edce-5933-a2e9-50797edcec0f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Big Eggsplosion",
            game_text="Flip a number of coins equal to the amount of Energy attached to Exeggutor. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=20),
        ),
        Attack(
            title="Lateral Eggsplosion",
            game_text="Flip a number of coins equal to the amount of Energy attached to all of of your Benched Pok\u00e9mon. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=_lateral_eggsplosion,
        ),
    ],
)