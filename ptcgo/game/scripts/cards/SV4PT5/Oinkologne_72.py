from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


async def follow_the_scent(ctx):
    heads = await ctx.flip_coins(3, "Follow the Scent")
    count = sum(1 for h in heads if h)
    discard = ctx.discard_pile()
    if count <= 0 or not discard:
        return
    picks = await ctx.choose_cards(
        discard, count, minimum=1,
        prompt=f"Choose up to {count} cards from your discard pile to put into your hand.",
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = PokemonCardDef(
    guid="f3a1c115-ba26-5aef-9461-94c7d4537e17",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name",
    display_name="Oinkologne",
    searchable_by=["Oinkologne", "Stage 1", "Oinkologne"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV4PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name",
    family_id=915,
    abilities=[
        Attack(
            title="Finest Selection",
            game_text="Flip 3 coins. Put a number of cards up to the number of heads from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=follow_the_scent,
        ),
        Attack(
            title="Perfume Press",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)