from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import named_one_of


async def signs_of_evolution(ctx):
    """One Dratini, one Dragonair and one Dragonite -- three separate slots,
    so a third Dratini cannot stand in for the Dragonite."""
    picked = await ctx.search_deck_groups(
        [(named_one_of("Dratini"), 1, "Dratini"),
         (named_one_of("Dragonair"), 1, "Dragonair"),
         (named_one_of("Dragonite"), 1, "Dragonite")],
        "Search your deck for a Dratini, a Dragonair and a Dragonite")
    cards = [card for group in picked for card in group]
    if cards:
        await ctx.put_in_hand(cards, reveal=True)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="8da26bbe-3e6a-51a6-a9b3-499f1b0ffa38",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for a Dratini, a Dragonair, and a Dragonite, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=signs_of_evolution,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)