from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, is_energy_card, named
from ptcgo.game.card_effects.attacks_common import condition_attack, mill_scaled_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="9895ae46-d962-5418-b304-2d122071cb8e",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1", "Whiscash"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Landslip",
            game_text="Discard the top 3 cards of your deck. This attack does 100 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="x",
            effect=mill_scaled_damage(3, 100, pred=is_energy_card),
        ),
    ],
)