from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per
from ptcgo.game.card_effects.passives_common import is_in_active_spot, retreat_free_when
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import attach_from_discard


def _basic_free_retreat(pokemon, carrier) -> bool:
    return (pokemon.owning_player_id == carrier.owning_player_id
            and "Basic" in subtypes_for(pokemon.archetype_id))


def _is_basic_energy(card) -> bool:
    return (is_energy_card(card)
            and not card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


def _is_benched(pokemon) -> bool:
    return not is_in_active_spot(pokemon)

card = PokemonCardDef(
    guid="d3b3138d-324c-5157-a369-dcbd0ef91c7b",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SilvallyGX.Name",
    display_name="Silvally-GX",
    searchable_by=["Silvally-GX", "Stage 1", "GX", "SilvallyGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=91,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TypeNull.Name",
    family_id=773,
    abilities=[
        Ability(
            title="Gyro Unit",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            passive=retreat_free_when(_basic_free_retreat),
        ),
        Attack(
            title="Turbo Drive",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=attach_from_discard(_is_basic_energy, count=1, target=_is_benched),
        ),
        Attack(
            title="Rebel-GX",
            game_text="This attack does 50 damage for each of your opponent's Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_bench("opponent"), 50),
        ),
    ],
)