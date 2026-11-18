from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, is_energy_card, named
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c02b85b-0e4d-5d5f-92f8-0584e57ea8a4",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name",
    display_name="Avalugg",
    searchable_by=["Avalugg", "Stage 1", "Avalugg"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Attack(
            title="Iceberg Breaker",
            game_text="Discard the top 6 cards of your deck, and this attack does 60 damage for each Basic Water Energy card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="x",
            effect=mill_scaled_damage(6, 60, pred=basic_energy_of("water")),
        ),
        Attack(
            title="Frost Stamp",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)