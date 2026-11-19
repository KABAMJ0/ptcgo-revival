from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="b7cea7f0-f96b-5813-85c0-f15675900072",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivireex.Name",
    display_name="Electivire ex",
    searchable_by=["Electivire ex", "Stage 1", "ex", "Electivireex"],
    subtypes=["Stage 1", "ex"],
    collector_number=212,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Dual Bolt",
            game_text="This attack does 50 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(50, pool="any", count=2, apply_modifiers=False),
        ),
        Attack(
            title="High-Voltage Press",
            game_text="If this Pok\u00e9mon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)