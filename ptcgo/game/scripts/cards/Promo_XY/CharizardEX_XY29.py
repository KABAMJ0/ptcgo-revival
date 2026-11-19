from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import search_attach_energy

def _basic_energy_card(card):
    """Basic Energy as printed on a DECK card (IS_SPECIAL_ENERGY is only set on
    attached cards, so `passives.is_basic_energy` matches every deck card)."""
    from ptcgo.game.card_effects.pokemon import is_energy_card
    return is_energy_card(card) and not bool(card.get_attribute(AttrID.IS_SPECIAL_ENERGY))


card = PokemonCardDef(
    guid="fbddc2d6-c841-51ff-8dec-0ad754620a9a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    display_name="Charizard-EX",
    searchable_by=["Charizard-EX", "Basic", "EX", "CharizardEX"],
    subtypes=["Basic", "EX"],
    collector_number=29,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=6,
    abilities=[
        Attack(
            title="Stoke",
            game_text="Flip a coin. If heads, search your deck for up to 3 basic Energy cards and attach them to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=search_attach_energy(_basic_energy_card, 3, to_self=True)),
        ),
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)