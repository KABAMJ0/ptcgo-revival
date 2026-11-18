from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from ptcgo.game.card_effects.attacks_common import (
    condition_attack, discard_random_from_hand,
)


async def two_headed_crushing(ctx):
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, 1)
    await ctx.discard_cards(ctx.deck_top(1, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="2533e6b0-c18b-5208-8b17-752e9bfb2b4c",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillainex.Name",
    display_name="Scovillain ex",
    searchable_by=["Scovillain ex", "Stage 1", "ex", "Scovillainex"],
    subtypes=["Stage 1", "ex"],
    collector_number=22,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=952,
    abilities=[
        Attack(
            title="Chili Snapper Bind",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.BURNED, no_retreat=True),
        ),
        Attack(
            title="Two-Headed Crushing",
            game_text="Discard a random card from your opponent's hand. Discard the top card of your opponent's deck.",
            cost={PokemonTypes.GRASS: 2},
            damage=140,
            effect=two_headed_crushing,
        ),
    ],
)