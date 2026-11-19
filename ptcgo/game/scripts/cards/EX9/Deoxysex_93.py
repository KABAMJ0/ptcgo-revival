from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import identity_swap_from_deck
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="39b0b6a5-08f3-582e-b79c-41cd3a3da53b",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxysex.Name",
    display_name="Deoxys ex",
    searchable_by=["Deoxys ex", "Basic", "ex", "Deoxysex"],
    subtypes=["Basic", "ex"],
    collector_number=93,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Form Change",
            game_text="Once during your turn (before your attack), you may search your deck for another Deoxys ex and switch it with Deoxys ex. (Any cards attached to Deoxys ex, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) If you do, put Deoxys ex on top of your deck. Shuffle your deck afterward. You can't use more than 1 Form Change Pok\u00e9-Power each turn.",
            effect=identity_swap_from_deck("Deoxys ex"),
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Fastwave",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)