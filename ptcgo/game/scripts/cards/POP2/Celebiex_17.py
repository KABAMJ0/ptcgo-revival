from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.pokemon import is_pokemon_ex
from ptcgo.game.card_effects.support_common import recover_from_discard

card = PokemonCardDef(
    guid="34cef53e-9c45-578c-9730-3f7febe366f5",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebiex.Name",
    display_name="Celebi ex",
    searchable_by=["Celebi ex", "Basic", "ex", "Celebiex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=251,
    abilities=[
        Ability(
            title="Time Reversal",
            game_text="Once during your turn, when you put Celebi ex from your hand onto your Bench, you may search your discard pile for a card, show it to your opponent, and put it on top of your deck.",
            trigger=Triggers.ON_PLAY,
            effect=recover_from_discard(count=1, to="deck_top"),
        ),
        Attack(
            title="Psychic Shield",
            game_text="Prevent all effects of attacks, including damage, done to Celebi ex by your opponent's Pok\u00e9mon-ex during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=protect_next_turn(prevent=True, effects_too=True,
                                     attacker_pred=is_pokemon_ex),
        ),
    ],
)