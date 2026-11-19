from ptcgo.game.card_effects.attacks_common import reduce_defender_attacks
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a99e8b23-08c4-5c60-a328-bb7c4ee97836",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlutterMane.Name",
    display_name="Flutter Mane",
    searchable_by=["Flutter Mane", "Basic", "Ancient", "FlutterMane"],
    subtypes=["Basic", "Ancient"],
    collector_number=96,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=987,
    abilities=[
        Attack(
            title="Perplexing Transfer",
            game_text="Move all damage counters from 1 of your Benched Ancient Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Moonblast",
            game_text="During your opponent's next turn, attacks used by the Defending Pok\u00e9mon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=70,
            effect=reduce_defender_attacks(30),
        ),
    ],
)