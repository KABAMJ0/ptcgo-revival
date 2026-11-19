from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on, condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

card = PokemonCardDef(
    guid="45d5f3ea-4855-5ddc-af0b-3e06b35f83ca",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BruteBonnet.Name",
    display_name="Brute Bonnet",
    searchable_by=["Brute Bonnet", "Basic", "Ancient", "BruteBonnet"],
    subtypes=["Basic", "Ancient"],
    collector_number=118,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=986,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Relentless Punches",
            game_text="This attack does 50 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=50,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 50, base=50),
        ),
    ],
)