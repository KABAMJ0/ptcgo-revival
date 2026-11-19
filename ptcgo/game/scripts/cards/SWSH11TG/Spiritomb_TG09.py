from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, count_discard


def _is_spiritomb(card):
    definition = def_for(card.archetype_id)
    return definition is not None and getattr(definition, "display_name", None) == "Spiritomb"


async def cursed_message(ctx):
    """If Knocked Out by damage from an attack from your opponent's Pokemon:
    search the deck for a card and put it into your hand. Then shuffle."""
    if not ctx.ko_from_attack:
        return
    picks = await ctx.search_deck(
        count=1, minimum=0, prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


chain_of_spirits = damage_per(count_discard("mine", _is_spiritomb), 60, base=10)

card = PokemonCardDef(
    guid="5cf7d308-79ab-5bca-a516-d51a1a5f3425",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Ability(
            title="Cursed Message",
            game_text="If this Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for a card and put it into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=cursed_message,
        ),
        Attack(
            title="Chain of Spirits",
            game_text="This attack does 60 more damage for each Spiritomb in your discard pile.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=10,
            damage_operator="+",
            effect=chain_of_spirits,
        ),
    ],
)