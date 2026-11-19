from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import named_one_of

_SWORD = named_one_of("Honedge", "Doublade", "Aegislash")


async def weaponized_swords(ctx):
    """Reveal any number of Honedge, Doublade and Aegislash from your
    hand; 60 damage for each card revealed."""
    swords = [card for card in ctx.hand() if _SWORD(card)]
    if not swords:
        return
    picks = await ctx.choose_cards(
        swords, len(swords), minimum=0,
        prompt="Reveal any number of Honedge, Doublade, and Aegislash from your hand",
    )
    if not picks:
        return
    await ctx.reveal_cards(picks)
    await ctx.deal_damage(60 * len(picks))


card = PokemonCardDef(
    guid="13c986ea-7ebd-5b97-97c9-feabdc0272bd",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    display_name="Doublade",
    searchable_by=["Doublade", "Stage 1", "Doublade"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name",
    family_id=679,
    abilities=[
        Attack(
            title="Weaponized Swords",
            game_text="Reveal any number of Honedge, Doublade, and Aegislash from your hand, and this attack does 60 damage for each card you revealed in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=weaponized_swords,
        ),
    ],
)