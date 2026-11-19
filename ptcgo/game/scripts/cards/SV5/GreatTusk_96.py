from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bench_has_damage_counters, bonus_if
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd9e7140-2dc9-57d7-82e8-19f8fc5aa5b0",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTusk.Name",
    display_name="Great Tusk",
    searchable_by=["Great Tusk", "Basic", "Ancient", "GreatTusk"],
    subtypes=["Basic", "Ancient"],
    collector_number=96,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Wrathful Charge",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=bonus_if(bench_has_damage_counters, 80),
        ),
    ],
)