from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def all_you_can_yeet(ctx):
    """Discard any number of cards from your hand (the whole effect)."""
    hand = ctx.hand()
    if not hand:
        return
    picks = await ctx.choose_cards(hand, len(hand), minimum=0,
                                   prompt="Discard any number of cards")
    if picks:
        await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="714b5cf0-5cad-596f-9f7b-a70f078fe03a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=79,
    abilities=[
        Attack(
            title="All-You-Can-Yeet",
            game_text="You may discard any number of cards from your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=all_you_can_yeet,
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)