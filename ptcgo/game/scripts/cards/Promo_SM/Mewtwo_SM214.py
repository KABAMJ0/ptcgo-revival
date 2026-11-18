from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.support_common import recover_from_discard


def _is_supporter(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.SUPPORTER.value

card = PokemonCardDef(
    guid="58de1262-e972-54ea-9e6f-182eb64eb3ac",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=214,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Ability(
            title="Mind Report",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may put a Supporter card from your discard pile on top of your deck.",
            effect=recover_from_discard(_is_supporter, count=1, to="deck_top"),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Psyshock",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)