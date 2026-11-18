from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _tail_fishing(ctx):
    """Flip a coin: heads searches out a card, tails discards one from hand."""
    heads = await ctx.flip_coins(1, "Tail-Fishing")
    if heads and heads[0]:
        picks = await ctx.search_deck(
            None, count=1, minimum=0,
            prompt="Choose a card to put into your hand.",
        )
        await ctx.put_in_hand(picks, reveal=False)
        await ctx.shuffle_deck()
    else:
        await ctx.discard_from_hand(1)

card = PokemonCardDef(
    guid="30cfab2d-8551-5fcc-af64-64fa15723e88",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="Tail-Fishing",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Then, shuffle your deck. If tails, discard a card from your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_tail_fishing,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
        ),
    ],
)