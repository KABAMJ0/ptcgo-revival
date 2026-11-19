from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_baby_effect, _baby_in_hand = baby_evolution("Electabuzz")
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="5dee685c-1436-5982-8a92-f55515203d20",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid δ",
    searchable_by=["Elekid \u03b4", "Basic", "Elekid"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=239,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Electabuzz from your hand onto Elekid (this counts as evolving Elekid) and remove all damage counters from Elekid.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Thunder Spear",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(10, pool="any"),
        ),
    ],
)