from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _gold_coffin(ctx):
    """Knocked Out by attack damage: search the deck for a card into hand."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(
        None, count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="827a087d-3f25-5142-87ce-228bef540fe3",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigusex.Name",
    display_name="Cofagrigus ex",
    searchable_by=["Cofagrigus ex", "Stage 1", "ex", "Cofagrigusex"],
    subtypes=["Stage 1", "ex"],
    collector_number=224,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Gold Coffin",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_gold_coffin,
        ),
        Attack(
            title="Hollow Hands",
            game_text="Put 5 damage counters on your opponent's Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=110,
            effect=unimplemented,
        ),
    ],
)