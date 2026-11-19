from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import remove_self_from_play, search_to_hand
from ptcgo.game.session.effects import is_supporter_card

card = PokemonCardDef(
    guid="9858bd57-f335-58a9-a8f3-0a418f9d6d3f",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowthex.Name",
    display_name="Meowth ex",
    searchable_by=["Meowth ex", "Basic", "ex", "Meowthex"],
    subtypes=["Basic", "ex"],
    collector_number=121,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Ability(
            title="Last-Ditch Catch",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand onto your Bench, you may use this Ability. Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck. You can't use more than 1 Ability that has \"Last-Ditch\" in its name each turn.",
            trigger=Triggers.ON_PLAY,
            shared_once_per_turn="Last-Ditch Catch",
            effect=search_to_hand(is_supporter_card, count=1, reveal=True),
        ),
        Attack(
            title="Tuck Tail",
            game_text="Put this Pok\u00e9mon and all attached cards into your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=remove_self_from_play(destination="hand", with_attachments="same"),
        ),
    ],
)