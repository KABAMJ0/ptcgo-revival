from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.pokemon import is_energy_card


async def flare_destroy(ctx):
    """70; one Energy off Typhlosion and one off the Defending Pokemon."""
    await ctx.deal_damage(70)
    await ctx.discard_energy_from(ctx.attacker, 1)
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(defender, 1)


def _fire_energy(card) -> bool:
    return is_energy_card(card) and PokemonTypes.FIRE.value in (
        card.get_attribute(AttrID.POKEMON_TYPES) or [])


def _afterburner():
    """Discard pile -> 1 of your Pokemon, then 1 damage counter on that one.

    The counter rides the holder `attach_from_discard` chose, which it hands back
    as (card, holder) pairs -- the pairs only contain cards that really attached."""
    async def effect(ctx):
        pairs = await attach_from_discard(
            predicate=_fire_energy, target="choice")(ctx)
        for _card, holder in pairs or []:
            await ctx.place_damage_counters(1, [holder])

    return effect


card = PokemonCardDef(
    guid="b62eba0b-6363-5703-bbae-3d415518b972",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Prime", "Typhlosion"],
    subtypes=["Stage 2", "Prime"],
    collector_number=9,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=157,
    abilities=[
        Ability(
            title="Afterburner",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you do, put 1 damage counter on that Pok\u00e9mon. This power can't be used if Typhlosion is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            effect=_afterburner(),
        ),
        Attack(
            title="Flare Destroy",
            game_text="Discard an Energy card attached to Typhlosion and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=flare_destroy,
        ),
    ],
)
