from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _ball_of_flame(ctx):
    """Ball of Flame: printed damage, or 20 on a Benched Pokemon for a Fire."""
    fire = [e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.FIRE.value)]
    bench = ctx.opponent_bench()
    if not fire or not bench or not await ctx.ask_yes_no(
            "Discard a Fire Energy to do 20 damage to a Benched Pokemon?"):
        await ctx.deal_damage()
        return
    await ctx.discard_cards(fire[:1])
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=False)
    await ctx.deal_damage()

from ptcgo.game.data_utils import Triggers


async def hot_plate(ctx):
    """A Basic or Baby Pokemon put onto either Bench from hand takes 10 with no
    Weakness or Resistance."""
    benched = getattr(ctx, "benched_pokemon", None)
    if benched is None:
        return
    await ctx.deal_damage(10, target=benched, apply_modifiers=False)

card = PokemonCardDef(
    guid="d98f82a6-1051-5e84-ab42-3507c800e4b6",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkMagcargo.Name",
    display_name="Dark Magcargo",
    searchable_by=["Dark Magcargo", "Stage 1", "DarkMagcargo"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Hot Plate",
            game_text="As long as Dark Magcargo is your Active Pok\u00e9mon, whenever a player puts a Baby Pok\u00e9mon or Basic Pok\u00e9mon onto his or her Bench from his or her hand, this power does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance.) This power stops working if Dark Magcargo is Asleep, Confused, or Paralyzed.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=hot_plate,
        ),
        Attack(
            title="Ball of Flame",
            game_text="You may discard a Fire Energy card attached to Dark Magcargo when you use this attack. If you do and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 20 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=_ball_of_flame,
        ),
    ],
)