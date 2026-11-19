from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot


async def moomoo_malt(ctx):
    """While this Pokemon is Active, an Energy card attached from hand heals
    90 damage from the Pokemon it was attached to."""
    if ctx.attaching_player_id != ctx.player_id:
        return
    if not is_in_active_spot(ctx.source):
        return
    receiver = ctx.energy_receiver
    if receiver is None or receiver.get_attribute(AttrID.HP, 0) <= 0:
        return
    await ctx.heal(90, receiver)


card = PokemonCardDef(
    guid="5195c3a2-ae4c-57c4-9cb5-3af770586221",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Ability(
            title="Moomoo Malt",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever you attach an Energy card from your hand to 1 of your Pok\u00e9mon, heal 90 damage from that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=moomoo_malt,
        ),
        Attack(
            title="Sitdown Splash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)