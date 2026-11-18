from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard


def _is_psychic_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="e8fbdd68-2a45-5524-b033-da91d5b36017",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=687,
    abilities=[
        Ability(
            title="Psychic Recharge",
            game_text="Once during your turn (before your attack), you may attach a Psychic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            effect=attach_from_discard(_is_psychic_energy, count=1,
                                       target=_is_benched),
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)