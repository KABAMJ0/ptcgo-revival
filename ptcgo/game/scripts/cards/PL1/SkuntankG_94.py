from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack

card = PokemonCardDef(
    guid="edd4b981-a6b5-5d63-abd6-6f33703a7f30",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkuntankG.Name",
    display_name="Skuntank G",
    searchable_by=["Skuntank G", "Basic", "SP", "SkuntankG"],
    subtypes=["Basic", "SP"],
    collector_number=94,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=435,
    abilities=[
        Ability(
            title="Poison Structure",
            game_text="Once during your turn (before your attack), if you have a Stadium card in play, you may use this power. Each Active Pok\u00e9mon (both yours and your opponent's) (excluding Pok\u00e9mon SP) is now Poisoned. This power can't be used if Skuntank is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=smokescreen_attack(),
        ),
    ],
)