from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_metal_energy_card


async def intrepid_sword(ctx):
    """Once per turn: look at the top 3, attach any Metal Energy found there
    to this Pokémon, the rest to hand. Ends your turn."""
    top = ctx.deck_top(3)
    if not top:
        return
    metal = [c for c in top if is_metal_energy_card(c)]
    # No matches still shows the looked-at cards (nothing selectable).
    picks = await ctx.choose_cards(
        metal, max(len(metal), 1), minimum=0,
        prompt="Attach any number of Metal Energy cards to this Pokémon.",
        display_cards=top,
    )
    for energy in picks:
        await ctx.attach_energy(energy, ctx.source)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.put_in_hand(rest, reveal=False)


card = PokemonCardDef(
    guid="3efcccdb-d897-56e4-8fd0-ee10b62e963a",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZacianV.Name",
    display_name="Zacian V",
    searchable_by=["Zacian V", "Basic", "V", "ZacianV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=888,
    abilities=[
        Ability(
            title="Intrepid Sword",
            game_text="Once during your turn, you may look at the top 3 cards of your deck and attach any number of Metal Energy cards you find there to this Pokémon. Put the other cards into your hand. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=intrepid_sword,
        ),
        Attack(
            title="Brave Blade",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 3},
            damage=230,
            locks_next_turn=True,
        ),
    ],
)
