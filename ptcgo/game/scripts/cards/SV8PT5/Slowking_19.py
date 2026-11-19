from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _aqua_wash(ctx):
    await ctx.deal_damage()
    active = ctx.opponent_active()
    energies = ctx.attached_energies(active) if active is not None else []
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Put 2 Energy attached to your opponent's Active Pokémon into their hand?"
    ):
        return
    picks = await ctx.choose_cards(
        energies, 2, prompt="Choose Energy to put into their hand"
    )
    await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="bc210f12-a2ef-55e6-8d24-8688dcd1278e",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Attack(
            title="Wash the Slate Clean",
            game_text="You may put 2 Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_aqua_wash,
        ),
    ],
)