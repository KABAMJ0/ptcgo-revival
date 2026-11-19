from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_attach_energy, swap_with_named
from ptcgo.game.scripts.cards import loader as card_loader

_CASTFORM_FORMS = {"castform", "rain castform", "snow-cloud castform"}


def _is_castform_form(card):
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() \
        in _CASTFORM_FORMS


def _is_holon_energy(card):
    definition = card_loader.cards_by_guid.get(
        (getattr(card, "archetype_id", "") or "").lower())
    return definition is not None and \
        (getattr(definition, "display_name", "") or "").lower().startswith("holon energy")


async def _shuffle_away_outgoing(ctx, incoming):
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="dc578eb4-9a59-5cd6-adbc-c5016da22a42",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SunnyCastform.Name",
    display_name="Sunny Castform",
    searchable_by=["Sunny Castform", "Basic", "SunnyCastform"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Rain Castform, or Snow-cloud Castform and switch it with Sunny Castform. (Any cards attached to Sunny Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Sunny Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperamental Weather",
            effect=swap_with_named(predicate=_is_castform_form, destination="deck",
                                   then=_shuffle_away_outgoing),
        ),
        Attack(
            title="Holon Search",
            game_text="Search your deck for a Holon Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_attach_energy(_is_holon_energy, count=1, to_self=False,
                                        distribute=False),
        ),
    ],
)