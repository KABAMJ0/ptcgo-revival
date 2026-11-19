from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import damage_per, count_energy
card = PokemonCardDef(
    guid="e9ef1ef6-f187-520d-9ceb-6ce9f6d4b646",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StarmieV.Name",
    display_name="Starmie V",
    searchable_by=["Starmie V", "Basic", "V", "StarmieV"],
    subtypes=["Basic", "V"],
    collector_number=13,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=121,
    abilities=[
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True, ignore_target_effects=True),
        ),
        Attack(
            title="Energy Spiral",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 50),
        ),
    ],
)