from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, \
    def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.support_common import swap_with_named


_WEATHER_FORMS = ("castform", "sunny castform", "snow-cloud castform")


def _display_name(card) -> str:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower()


def _is_weather_form(card) -> bool:
    """Castform, Sunny Castform or Snow-cloud Castform -- the deck copies
    Temperamental Weather may swap in."""
    return _display_name(card) in _WEATHER_FORMS


def _is_holon_energy(card) -> bool:
    return _display_name(card).startswith("holon energy")


def _holon_attached(ctx) -> int:
    return sum(1 for energy in ctx.attached_energies(ctx.attacker)
               if _is_holon_energy(energy))


card = PokemonCardDef(
    guid="dfae2e5a-ee7f-5917-8842-ba424979394e",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RainCastform.Name",
    display_name="Rain Castform",
    searchable_by=["Rain Castform", "Basic", "RainCastform"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Sunny Castform, or Snow-cloud Castform and switch it with Rain Castform. (Any cards attached to Rain Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Rain Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Temperamental Weather",
            effect=swap_with_named(predicate=_is_weather_form),
        ),
        Attack(
            title="Holon Splash",
            game_text="Does 30 damage plus 10 more damage for each Holon Energy card attached to Rain Castform.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(_holon_attached, 10, base=30),
        ),
    ],
)