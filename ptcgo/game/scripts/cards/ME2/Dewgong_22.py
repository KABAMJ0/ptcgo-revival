from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.passives_common import pokemon_of_types, takes_less_passive

card = PokemonCardDef(
    guid="1610ff33-bfd8-5787-af95-5859ba71ef02",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks from your opponent's Fire or Water Pok\u00e9mon (after applying Weakness and Resistance).",
            passive=takes_less_passive(
                30, attacker_pred=pokemon_of_types(
                    PokemonTypes.FIRE.value, PokemonTypes.WATER.value)),
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=70),
        ),
    ],
)