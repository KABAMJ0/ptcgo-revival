from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, snipe_attack, spread_damage, place_counters
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ff592e32-8041-53c4-8f80-130195cd2d06",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmotex.Name",
    display_name="Pawmot ex",
    searchable_by=["Pawmot ex", "Stage 2", "ex", "Pawmotex"],
    subtypes=["Stage 2", "ex"],
    collector_number=73,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=923,
    abilities=[
        Attack(
            title="Zap Kick",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title="Levin Strike",
            game_text="Discard 2 Lightning Energy from this Pok\u00e9mon. This attack does 220 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.LIGHTNING, before_damage=True, also=snipe_attack(220, pool="any", count=1)),
        ),
    ],
)