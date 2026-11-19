from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bench_has_damage_counters, bonus_if
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks

card = PokemonCardDef(
    guid="a288d9bf-f57f-5ca0-9d24-43cb1fd74c33",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mabosstiffex.Name",
    display_name="Mabosstiff ex",
    searchable_by=["Mabosstiff ex", "Stage 1", "ex", "Mabosstiffex"],
    subtypes=["Stage 1", "ex"],
    collector_number=86,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Maschiff.Name",
    family_id=942,
    abilities=[
        Attack(
            title="Daunt",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 50 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=reduce_defender_attacks(50),
        ),
        Attack(
            title="Proud Fangs",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(bench_has_damage_counters, 120),
        ),
    ],
)