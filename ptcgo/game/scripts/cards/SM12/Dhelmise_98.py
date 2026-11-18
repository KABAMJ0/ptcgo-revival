from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, CardType
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import recover_from_discard


def _is_trainer_card(card) -> bool:
    return card.get_attribute(AttrID.CARD_TYPE) == CardType.TRAINER.value

card = PokemonCardDef(
    guid="1c7c0d32-0a52-5669-909f-772c1cb84a48",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=781,
    abilities=[
        Attack(
            title="Seaweed Grab",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(_is_trainer_card),
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=ignore_modifier_attack(ignore_resistance=True),
        ),
    ],
)