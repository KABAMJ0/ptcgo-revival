from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import flip_damage_condition, place_counters
from ptcgo.game.card_effects.passives_common import unafflicted

card = PokemonCardDef(
    guid="6c66ec83-1989-57a9-9f40-266ec2aa8997",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crobatex.Name",
    display_name="Crobat ex",
    searchable_by=["Crobat ex", "Stage 2", "ex", "Crobatex"],
    subtypes=["Stage 2", "ex"],
    collector_number=96,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name",
    family_id=41,
    abilities=[
        Ability(
            title="Distortion",
            game_text="Once during your turn (before your attack), if Crobat ex is your Active Pok\u00e9mon, you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon. This power can't be used if Crobat ex is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=place_counters(1, target="choose_any_opponent"),
        ),
        Attack(
            title="Cross Attack",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads. If you get 2 or more heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage_condition(coins=4, per_heads=20, min_heads=2,
                                         condition=SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Pester",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 60 damage plus 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)