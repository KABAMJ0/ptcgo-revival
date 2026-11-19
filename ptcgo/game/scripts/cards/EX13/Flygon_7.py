from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="39e04ca3-2d7a-5bd7-99bd-18e05ead4213",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon δ",
    searchable_by=["Flygon \u03b4", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=330,
    abilities=[
        Ability(
            title="Delta Supply",
            game_text="Once during your turn (before your attack), you may attach a basic Energy card or a \u03b4 Rainbow Energy card from your hand to 1 of your Pok\u00e9mon that has \u03b4 on its card. This power can't be used if Flygon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)