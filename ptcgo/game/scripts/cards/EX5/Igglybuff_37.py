from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Jigglypuff")

card = PokemonCardDef(
    guid="c1509a87-c406-570d-b498-254355ab009a",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Basic", "Igglybuff"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=174,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Jigglypuff from your hand onto Igglybuff (this counts as evolving Igglybuff), and remove all damage counters from Igglybuff.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Set Song",
            game_text="Search your deck for a Basic Pok\u00e9mon and a basic Energy card, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)