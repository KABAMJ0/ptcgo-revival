from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="6206d2a1-dff5-57e6-abc9-24487f6ea918",
    key="POP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxysex.Name",
    display_name="Deoxys ex",
    searchable_by=["Deoxys ex", "Basic", "ex", "Deoxysex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP4",
    rarity=Rarities.Rare,
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
            effect=unimplemented,
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