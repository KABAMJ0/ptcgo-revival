from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="2cb52001-8342-5af8-8e6a-5c3e9cc835e1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysStaryu.Name",
    display_name="Misty's Staryu",
    searchable_by=["Misty's Staryu", "Basic", "MistysStaryu"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, Pok\u00e9mon Powers, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)