from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import evolution_lock_passive
from ptcgo.game.card_effects.support_common import opponent_switches


async def drag_off(ctx):
    target = None
    if ctx.opponent_bench() and await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with the Defending Pokémon?"):
        target = await opponent_switches(ctx)
    await ctx.deal_damage(target=target)


card = PokemonCardDef(
    guid="ea4becb3-1517-5f11-85bc-316da56fc2ef",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kabutops.Name",
    display_name="Kabutops",
    searchable_by=["Kabutops", "Stage 2", "Kabutops"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name",
    family_id=140,
    abilities=[
        Ability(
            title="Primal Stare",
            game_text="As long as Kabutops is your Active Pok\u00e9mon, your opponent can't play any Basic Pok\u00e9mon or Evolution cards from his or her hand to evolve his or her Active Pok\u00e9mon.",
            passive=evolution_lock_passive(active_only=True),
        ),
        Attack(
            title="Luring Antenna",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. If you do, this attack does 20 damage to the new Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=drag_off,
        ),
        Attack(
            title="Blinding Scythe",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)