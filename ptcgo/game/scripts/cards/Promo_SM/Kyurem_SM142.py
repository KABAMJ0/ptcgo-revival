from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per, snipe_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="78c2051c-536b-534f-82b6-caaf2ae5a958",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyurem.Name",
    display_name="Kyurem",
    searchable_by=["Kyurem", "Basic", "Kyurem"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=646,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), per=10, base=20),
        ),
        Attack(
            title="Frost Spear",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=snipe_attack(20, pool="bench", count=1, apply_modifiers=False),
        ),
    ],
)