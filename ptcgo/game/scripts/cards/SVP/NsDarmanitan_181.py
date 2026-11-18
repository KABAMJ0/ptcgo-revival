from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters, damage_per, count_discard
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="10f98ed8-1565-584e-a890-356aecf2626b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarmanitan.Name",
    display_name="N's Darmanitan",
    searchable_by=["N's Darmanitan", "Stage 1", "NsDarmanitan"],
    subtypes=["Stage 1"],
    collector_number=181,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarumaka.Name",
    family_id=555,
    abilities=[
        Attack(
            title="Back Draft",
            game_text="This attack does 30 damage for each Basic Energy card in your opponent's discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_discard("opponent", is_basic_energy_card), per=30),
        ),
        Attack(
            title="Flamebody Cannon",
            game_text="Discard all Energy from this Pok\u00e9mon, and this attack also does 90 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=self_energy_discard_attack(all_energy=True, before_damage=True, also=snipe_attack(90, pool="bench", count=1)),
        ),
    ],
)