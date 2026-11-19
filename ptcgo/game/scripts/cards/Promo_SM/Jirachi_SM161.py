from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, SpecialConditions
from ptcgo.game.card_effects.pokemon import in_active_spot

async def stellar_wish(ctx):
    """Look at the top 5 cards; one Trainer card goes to hand, the rest go back
    in any order."""
    from ptcgo.game.attributes import CardType
    cards = await ctx.reveal_top(5)
    if not cards:
        return
    trainers = [c for c in cards
                if c.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value]
    picks = await ctx.choose_cards(trainers, 1, prompt="Choose a Trainer card") if trainers else []
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    rest = [c for c in cards if c not in (picks or [])]
    if rest:
        await ctx.shuffle_into_deck(rest)
    await ctx.apply_special_condition(ctx.source, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="dc9a330b-7f83-53fa-b170-0a4a1edea705",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Ability(
            title="Stellar Wish",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may look at the top 5 cards of your deck, reveal a Trainer card you find there, and put it into your hand. Then, shuffle the other cards back into your deck, and this Pok\u00e9mon is now Asleep.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=stellar_wish,
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)