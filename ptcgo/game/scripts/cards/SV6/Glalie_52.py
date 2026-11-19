from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.attacks_common import damage_per, damage_counters_on


card = PokemonCardDef(
    guid="279d3ceb-8dbf-58a2-888f-6426afd76acf",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Damage Beat",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on('defender'), 20),
        ),
        Attack(
            title="Crazy Headbutt",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)