from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import typed_energy_free_retreat_passive

card = PokemonCardDef(
    guid="58a8ce0a-02a7-549a-abfd-67e4f7c85158",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Ability(
            title="Flare Float",
            game_text="If this Pok\u00e9mon has any Fire Energy attached, it has no Retreat Cost.",
            passive=typed_energy_free_retreat_passive(PokemonTypes.FIRE),
        ),
        Attack(
            title="Blazing Flight",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon. This attack does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 3},
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE, before_damage=True, also=snipe_attack(120, pool="bench", count=1)),
        ),
    ],
)