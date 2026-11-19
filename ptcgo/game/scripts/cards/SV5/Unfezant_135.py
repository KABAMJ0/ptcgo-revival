from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack


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
    guid="71a25a7f-669c-5a76-bdce-f01e3aa8aeb5",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=135,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Opposing Winds",
            game_text="You may put 2 Energy attached to your opponent's Active Pok\u00e9mon into their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_aqua_wash,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=lock_self_attack(),
        ),
    ],
)