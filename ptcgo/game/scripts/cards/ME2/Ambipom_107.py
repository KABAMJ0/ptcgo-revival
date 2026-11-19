from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae2e14cf-b50d-5a7d-82ac-484347bb2644",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1", "Ambipom"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Dual Tail",
            game_text="Discard 2 Energy from this Pok\u00e9mon, and this attack does 60 damage to each of 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=self_energy_discard_attack(count=2, before_damage=True, also=snipe_attack(60, pool="any", count=2)),
        ),
    ],
)