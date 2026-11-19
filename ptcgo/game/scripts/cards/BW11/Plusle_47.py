from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for


def _printed_name(pokemon):
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower()


async def tag_draw(ctx):
    """Shuffle your hand into your deck, draw 4, and 4 more with Minun on your
    Bench."""
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(4)
    if any(_printed_name(pokemon) == "minun" for pokemon in ctx.my_bench()):
        await ctx.draw_cards(4)


card = PokemonCardDef(
    guid="310b2601-b601-5c76-85e1-9b0a0886c83a",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=311,
    abilities=[
        Attack(
            title="Tag Draw",
            game_text="Shuffle your hand into your deck. Then, draw 4 cards. If Minun is on your Bench, draw 4 more cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=tag_draw,
        ),
        Attack(
            title="Positive Ion",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)