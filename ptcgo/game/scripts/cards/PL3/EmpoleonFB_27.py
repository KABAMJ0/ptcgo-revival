from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="0dadac9f-72c4-5644-8133-f407ec42cec8",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonFB.Name",
    display_name="Empoleon FB",
    searchable_by=["Empoleon FB", "Basic", "SP", "EmpoleonFB"],
    subtypes=["Basic", "SP"],
    collector_number=27,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=395,
    abilities=[
        Attack(
            title="Rushing Water",
            game_text="Move an Energy card attached to the Defending Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Escort",
            game_text="If you played any Supporter card from your hand during this turn, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)