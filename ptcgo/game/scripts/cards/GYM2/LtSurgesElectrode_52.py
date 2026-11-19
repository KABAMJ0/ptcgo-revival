from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba6253d1-6666-51c7-bbe7-9e85025bb572",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesElectrode.Name",
    display_name="Lt. Surge's Electrode",
    searchable_by=["Lt. Surge's Electrode", "Stage 1", "LtSurgesElectrode"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LtSurgesVoltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Shock Blast",
            game_text="If Lt. Surge's Electrode is your Active Pok\u00e9mon and gets damaged (even if it's Knocked Out), flip a coin. If tails, this power does 20 damage to each Active Pok\u00e9mon. This power works even if Lt. Surge's Electrode is already Asleep, Confused, or Paralyzed when it takes damage.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Ball",
            game_text="Flip 3 coins. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=3, per_heads=10, base=30),
        ),
    ],
)