from ptcgo.game.card_effects.attacks_common import snipe_attack, ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb0e78f0-767e-5975-ad95-451cf893ae56",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaStarmieex.Name",
    display_name="Mega Starmie ex",
    searchable_by=["Mega Starmie ex", "Stage 1", "MEGA", "ex", "MegaStarmieex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=21,
    set_code="ME3",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Jetting Blow",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            damage=120,
            effect=snipe_attack(50, pool="bench", count=1, apply_modifiers=False, also_base=True),
        ),
        Attack(
            title="Nebula Beam",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=210,
            effect=ignore_modifier_attack(
                ignore_weakness=True,
                ignore_resistance=True,
                ignore_target_effects=True,
            ),
        ),
    ],
)