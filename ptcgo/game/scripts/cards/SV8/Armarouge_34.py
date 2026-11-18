from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c70d4e63-6c80-583f-bfbe-de38dd976819",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1", "Armarouge"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Crimson Blaster",
            game_text="Discard all Fire Energy from this Pok\u00e9mon, and this attack does 180 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE, before_damage=True, also=snipe_attack(180, pool="bench", count=1)),
        ),
    ],
)