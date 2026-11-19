from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_gate, spread_damage

card = PokemonCardDef(
    guid="5b212fc2-459b-5ea1-8cd8-b6b937f72aba",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MamoswineGL.Name",
    display_name="Mamoswine GL",
    searchable_by=["Mamoswine GL", "Basic", "SP", "MamoswineGL"],
    subtypes=["Basic", "SP"],
    collector_number=27,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=473,
    abilities=[
        Ability(
            title="Icy Aura",
            game_text="As long as Mamoswine GL is your Active Pok\u00e9mon, put 1 damage counter on each Active Pok\u00e9mon (excluding Water Pok\u00e9mon) (both yours and your opponent's) between turns.",
            effect=unimplemented,
        ),
        Attack(
            title="Avalanche",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=flip_gate(then=spread_damage(10, side="opponent")),
        ),
    ],
)