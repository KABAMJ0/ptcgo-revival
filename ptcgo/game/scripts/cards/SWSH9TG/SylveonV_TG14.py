from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_item_card
card = PokemonCardDef(
    guid="5b5a955d-6272-50df-b08c-e514246c0378",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SylveonV.Name",
    display_name="Sylveon V",
    searchable_by=["Sylveon V", "Basic", "V", "Rapid Strike", "SylveonV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=14,
    set_code="SWSH9TG",
    rarity=Rarities.RareHoloV,
    hp=200,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=700,
    abilities=[
        Ability(
            title="Dream Gift",
            game_text="Once during your turn, you may search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck. If you use this Ability, your turn ends.",
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            effect=search_to_hand(is_item_card),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)