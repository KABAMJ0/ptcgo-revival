from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.trainers import all_of, basic_energy_of, is_energy_card, named
from ptcgo.game.card_effects.attacks_common import mill_scaled_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="cf720f0d-bc80-575d-8760-96d0cad33f51",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAbomasnowex.Name",
    display_name="Mega Abomasnow ex",
    searchable_by=["Mega Abomasnow ex", "Stage 1", "MEGA", "ex", "MegaAbomasnowex"],
    subtypes=["Stage 1", "MEGA", "ex"],
    collector_number=157,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=350,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Hammer-lanche",
            game_text="Discard the top 6 cards of your deck, and this attack does 100 damage for each Basic Water Energy card that you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=100,
            damage_operator="x",
            effect=mill_scaled_damage(6, 100, pred=basic_energy_of("water")),
        ),
        Attack(
            title="Frost Barrier",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=200,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)