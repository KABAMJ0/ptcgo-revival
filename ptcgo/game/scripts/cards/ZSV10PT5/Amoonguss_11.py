from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if, defender_has_any_condition
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c4ce8f81-eb80-5cdf-b409-c8b6b9fa5b36",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Dangerous Reaction",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(defender_has_any_condition, 120),
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)