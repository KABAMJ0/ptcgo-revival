from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID

async def night_scan(ctx):
    """Reveal the opponent's hand; 30 plus 30 for each Trainer card in it."""
    from ptcgo.game.attributes import CardType
    cards = await ctx.reveal_hand(ctx.opponent_id)
    trainers = sum(1 for c in (cards or [])
                   if c.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value)
    await ctx.deal_damage(30 + 30 * trainers)


card = PokemonCardDef(
    guid="04d44328-1750-5b76-bff9-bd42715bc00d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NoctowlBREAK.Name",
    display_name="Noctowl BREAK",
    searchable_by=["Noctowl BREAK", "BREAK", "NoctowlBREAK"],
    subtypes=["BREAK"],
    collector_number=136,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    family_id=164,
    abilities=[
        Attack(
            title="Night Scan",
            game_text="Your opponent reveals his or her hand. This attack does 30 more damage for each Trainer card you find there.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=night_scan,
        ),
    ],
)