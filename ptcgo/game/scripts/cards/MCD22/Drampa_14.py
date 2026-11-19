from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bench_has_damage_counters, bonus_if
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b689ccf-aebd-5983-8acd-541c29fe78b0",
    key="MCD22",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drampa.Name",
    display_name="Drampa",
    searchable_by=["Drampa", "Basic", "Drampa"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="MCD22",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=780,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Berserk",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="+",
            effect=bonus_if(bench_has_damage_counters, 90),
        ),
    ],
)