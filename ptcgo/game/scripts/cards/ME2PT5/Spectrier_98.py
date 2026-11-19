from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6cf39700-962c-509b-b86c-b88c28792d20",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spectrier.Name",
    display_name="Spectrier",
    searchable_by=["Spectrier", "Basic", "Spectrier"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=897,
    abilities=[
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Phantasmal Barrage",
            game_text="Discard all Energy from this Pok\u00e9mon and place 12 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            effect=self_energy_discard_attack(all_energy=True, before_damage=True, also=place_counters(12, target="choose_any_opponent")),
        ),
    ],
)