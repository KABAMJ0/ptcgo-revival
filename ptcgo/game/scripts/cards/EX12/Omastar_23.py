from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import opponent_switches

async def drag_off(ctx):
    target = None
    if ctx.opponent_bench() and await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with the Defending Pokémon?"):
        target = await opponent_switches(ctx)
    await ctx.deal_damage(target=target)


card = PokemonCardDef(
    guid="61ce97aa-e665-583d-b2b8-5f46d00c2278",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2", "Omastar"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Ancient Fang",
            game_text="As long as you have Kabuto, Kabutops, or Kabutops ex in play, Omastar's attacks do 20 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=drag_off,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)