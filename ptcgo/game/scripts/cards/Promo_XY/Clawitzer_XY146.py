from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, AttrID, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_hand

def _special_energy(card):
    from ptcgo.game.card_effects.pokemon import is_energy_card
    return is_energy_card(card) and bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_mega(pokemon):
    from ptcgo.game.data_utils import def_for
    return "MEGA" in [ (s or "").upper() for s in (getattr(def_for(pokemon.archetype_id), "subtypes", None) or [])]


async def mega_boost(ctx):
    """Attach a Special Energy card from hand to 1 of your Mega Evolution Pokemon."""
    await attach_from_hand(_special_energy, 1, target="choice", target_pred=_is_mega,
                           minimum=1,
                           prompt="Choose a Special Energy to attach")(ctx)


card = PokemonCardDef(
    guid="14575688-ec8e-552f-a5a1-f281e87a5798",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clawitzer.Name",
    display_name="Clawitzer",
    searchable_by=["Clawitzer", "Stage 1", "Clawitzer"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    family_id=693,
    abilities=[
        Ability(
            title="Mega Boost",
            game_text="Once during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Mega Evolution Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=mega_boost,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)