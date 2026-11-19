from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import swap_with_named
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.scripts.cards import loader as card_loader

_CASTFORM_FORMS = {"castform", "rain castform", "sunny castform"}


def _is_castform_form(card):
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() \
        in _CASTFORM_FORMS


async def _shuffle_away_outgoing(ctx, incoming):
    await ctx.shuffle_deck()


def _has_holon_energy(ctx):
    for energy in ctx.attached_energies(ctx.attacker):
        definition = card_loader.cards_by_guid.get((energy.archetype_id or "").lower())
        if definition is not None and \
                (getattr(definition, "display_name", "") or "").lower().startswith("holon energy"):
            return True
    return False


async def _holon_blizzard(ctx):
    await ctx.deal_damage()
    if _has_holon_energy(ctx):
        await spread_damage(10, side="opponent")(ctx)


card = PokemonCardDef(
    guid="760df7a4-564b-5faf-84a0-79e1dbfc21b8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnowcloudCastform.Name",
    display_name="Snow-cloud Castform",
    searchable_by=["Snow-cloud Castform", "Basic", "SnowcloudCastform"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Rain Castform, or Sunny Castform and switch it with Snow-cloud Castform. (Any cards attached to Snow-cloud Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Snow-cloud Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperamental Weather",
            effect=swap_with_named(predicate=_is_castform_form, destination="deck",
                                   then=_shuffle_away_outgoing),
        ),
        Attack(
            title="Holon Blizzard",
            game_text="If Snow-cloud Castform has any Holon Energy cards attached to it, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_holon_blizzard,
        ),
    ],
)