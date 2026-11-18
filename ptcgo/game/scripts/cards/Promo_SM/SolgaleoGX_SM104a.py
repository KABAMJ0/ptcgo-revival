from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import (
    is_in_active_spot,
    no_weakness_passive,
)
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard


def _protects_own_team(target, carrier) -> bool:
    return target.owning_player_id == carrier.owning_player_id


def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="ee061c8e-c817-58d6-b734-fa517b6a75bd",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=104,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=791,
    abilities=[
        Ability(
            title="Shining Mane",
            game_text="Your Pok\u00e9mon in play have no Weakness.",
            passive=no_weakness_passive(protects=_protects_own_team),
        ),
        Attack(
            title="Turbo Strike",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=attach_from_discard(_is_basic_energy, count=2, target=_is_benched),
        ),
        Attack(
            title="Prominence-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)